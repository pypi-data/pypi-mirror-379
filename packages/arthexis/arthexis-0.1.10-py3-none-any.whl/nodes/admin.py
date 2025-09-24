from django.contrib import admin, messages
from django.urls import path, reverse
from django.shortcuts import redirect, render
from django.utils.html import format_html
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from core.widgets import CopyColorWidget
from django.db.models import Count
from django.conf import settings
from pathlib import Path
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
import base64
import pyperclip
from pyperclip import PyperclipException
import uuid
import subprocess
from .utils import capture_screenshot, save_screenshot
from .actions import NodeAction

from .models import (
    Node,
    EmailOutbox,
    NodeRole,
    NodeFeature,
    NodeFeatureAssignment,
    ContentSample,
    NetMessage,
)
from core.user_data import EntityModelAdmin


class NodeAdminForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = "__all__"
        widgets = {"badge_color": CopyColorWidget()}


class NodeFeatureAssignmentInline(admin.TabularInline):
    model = NodeFeatureAssignment
    extra = 0
    autocomplete_fields = ("feature",)


@admin.register(Node)
class NodeAdmin(EntityModelAdmin):
    list_display = (
        "hostname",
        "mac_address",
        "address",
        "port",
        "role",
        "last_seen",
    )
    search_fields = ("hostname", "address", "mac_address")
    change_list_template = "admin/nodes/node/change_list.html"
    change_form_template = "admin/nodes/node/change_form.html"
    form = NodeAdminForm
    actions = ["register_visitor", "run_task", "take_screenshots"]
    inlines = [NodeFeatureAssignmentInline]

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "register-current/",
                self.admin_site.admin_view(self.register_current),
                name="nodes_node_register_current",
            ),
            path(
                "register-visitor/",
                self.admin_site.admin_view(self.register_visitor_view),
                name="nodes_node_register_visitor",
            ),
            path(
                "<int:node_id>/action/<str:action>/",
                self.admin_site.admin_view(self.action_view),
                name="nodes_node_action",
            ),
            path(
                "<int:node_id>/public-key/",
                self.admin_site.admin_view(self.public_key),
                name="nodes_node_public_key",
            ),
        ]
        return custom + urls

    def register_current(self, request):
        """Create or update this host and offer browser node registration."""
        node, created = Node.register_current()
        if created:
            self.message_user(
                request, f"Current host registered as {node}", messages.SUCCESS
            )
        token = uuid.uuid4().hex
        context = {
            "token": token,
            "register_url": reverse("register-node"),
        }
        return render(request, "admin/nodes/node/register_remote.html", context)

    @admin.action(description="Register Visitor Node")
    def register_visitor(self, request, queryset=None):
        return self.register_visitor_view(request)

    def register_visitor_view(self, request):
        """Exchange registration data with the visiting node."""

        node, created = Node.register_current()
        if created:
            self.message_user(
                request, f"Current host registered as {node}", messages.SUCCESS
            )

        token = uuid.uuid4().hex
        context = {
            **self.admin_site.each_context(request),
            "opts": self.model._meta,
            "title": _("Register Visitor Node"),
            "token": token,
            "info_url": reverse("node-info"),
            "register_url": reverse("register-node"),
            "visitor_info_url": "http://localhost:8000/nodes/info/",
            "visitor_register_url": "http://localhost:8000/nodes/register/",
        }
        return render(request, "admin/nodes/node/register_visitor.html", context)

    def public_key(self, request, node_id):
        node = self.get_object(request, node_id)
        if not node:
            self.message_user(request, "Unknown node", messages.ERROR)
            return redirect("..")
        security_dir = Path(settings.BASE_DIR) / "security"
        pub_path = security_dir / f"{node.public_endpoint}.pub"
        if pub_path.exists():
            response = HttpResponse(pub_path.read_bytes(), content_type="text/plain")
            response["Content-Disposition"] = f'attachment; filename="{pub_path.name}"'
            return response
        self.message_user(request, "Public key not found", messages.ERROR)
        return redirect("..")

    def run_task(self, request, queryset):
        if "apply" in request.POST:
            recipe_text = request.POST.get("recipe", "")
            results = []
            for node in queryset:
                try:
                    if not node.is_local:
                        raise NotImplementedError(
                            "Remote node execution is not implemented"
                        )
                    command = ["/bin/sh", "-c", recipe_text]
                    result = subprocess.run(
                        command,
                        check=False,
                        capture_output=True,
                        text=True,
                    )
                    output = result.stdout + result.stderr
                except Exception as exc:
                    output = str(exc)
                results.append((node, output))
            context = {"recipe": recipe_text, "results": results}
            return render(request, "admin/nodes/task_result.html", context)
        context = {"nodes": queryset}
        return render(request, "admin/nodes/node/run_task.html", context)

    run_task.short_description = "Run task"

    @admin.action(description="Take Screenshots")
    def take_screenshots(self, request, queryset):
        tx = uuid.uuid4()
        sources = getattr(settings, "SCREENSHOT_SOURCES", ["/"])
        count = 0
        for node in queryset:
            for source in sources:
                try:
                    url = source.format(node=node, address=node.address, port=node.port)
                except Exception:
                    url = source
                if not url.startswith("http"):
                    url = f"http://{node.address}:{node.port}{url}"
                try:
                    path = capture_screenshot(url)
                except Exception as exc:  # pragma: no cover - selenium issues
                    self.message_user(request, f"{node}: {exc}", messages.ERROR)
                    continue
                sample = save_screenshot(
                    path, node=node, method="ADMIN", transaction_uuid=tx
                )
                if sample:
                    count += 1
        self.message_user(request, f"{count} screenshots captured", messages.SUCCESS)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["node_actions"] = NodeAction.get_actions()
        if object_id:
            extra_context["public_key_url"] = reverse(
                "admin:nodes_node_public_key", args=[object_id]
            )
        return super().changeform_view(
            request, object_id, form_url, extra_context=extra_context
        )

    def action_view(self, request, node_id, action):
        node = self.get_object(request, node_id)
        action_cls = NodeAction.registry.get(action)
        if not node or not action_cls:
            self.message_user(request, "Unknown node action", messages.ERROR)
            return redirect("..")
        try:
            result = action_cls.run(node)
            if hasattr(result, "status_code"):
                return result
            self.message_user(
                request,
                f"{action_cls.display_name} executed successfully",
                messages.SUCCESS,
            )
        except NotImplementedError:
            self.message_user(
                request,
                "Remote node actions are not yet implemented",
                messages.WARNING,
            )
        except Exception as exc:  # pragma: no cover - unexpected errors
            self.message_user(request, str(exc), messages.ERROR)
        return redirect(reverse("admin:nodes_node_change", args=[node_id]))


@admin.register(EmailOutbox)
class EmailOutboxAdmin(EntityModelAdmin):
    list_display = ("owner_label", "host", "port", "username", "use_tls", "use_ssl")
    change_form_template = "admin/nodes/emailoutbox/change_form.html"
    fieldsets = (
        ("Owner", {"fields": ("user", "group", "node")}),
        (
            None,
            {
                "fields": (
                    "host",
                    "port",
                    "username",
                    "password",
                    "use_tls",
                    "use_ssl",
                    "from_email",
                )
            },
        ),
    )

    @admin.display(description="Owner")
    def owner_label(self, obj):
        return obj.owner_display()

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "<path:object_id>/test/",
                self.admin_site.admin_view(self.test_outbox),
                name="nodes_emailoutbox_test",
            )
        ]
        return custom + urls

    def test_outbox(self, request, object_id):
        outbox = self.get_object(request, object_id)
        if not outbox:
            self.message_user(request, "Unknown outbox", messages.ERROR)
            return redirect("..")
        recipient = request.user.email or outbox.username
        try:
            outbox.send_mail(
                "Test email",
                "This is a test email.",
                [recipient],
            )
            self.message_user(request, "Test email sent", messages.SUCCESS)
        except Exception as exc:  # pragma: no cover - admin feedback
            self.message_user(request, str(exc), messages.ERROR)
        return redirect("..")

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        if object_id:
            extra_context["test_url"] = reverse(
                "admin:nodes_emailoutbox_test", args=[object_id]
            )
        return super().changeform_view(request, object_id, form_url, extra_context)


class NodeRoleAdminForm(forms.ModelForm):
    nodes = forms.ModelMultipleChoiceField(
        queryset=Node.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Nodes", False),
    )

    class Meta:
        model = NodeRole
        fields = ("name", "description", "nodes")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["nodes"].initial = self.instance.node_set.all()


@admin.register(NodeRole)
class NodeRoleAdmin(EntityModelAdmin):
    form = NodeRoleAdminForm
    list_display = ("name", "description", "registered", "default_features")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_registered=Count("node", distinct=True)).prefetch_related(
            "features"
        )

    @admin.display(description="Registered", ordering="_registered")
    def registered(self, obj):
        return getattr(obj, "_registered", obj.node_set.count())

    @admin.display(description="Default Features")
    def default_features(self, obj):
        features = [feature.display for feature in obj.features.all()]
        return ", ".join(features) if features else "—"

    def save_model(self, request, obj, form, change):
        obj.node_set.set(form.cleaned_data.get("nodes", []))


@admin.register(NodeFeature)
class NodeFeatureAdmin(EntityModelAdmin):
    filter_horizontal = ("roles",)
    list_display = ("display", "slug", "default_roles", "is_enabled")
    readonly_fields = ("is_enabled",)
    search_fields = ("display", "slug")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("roles")

    @admin.display(description="Default Roles")
    def default_roles(self, obj):
        roles = [role.name for role in obj.roles.all()]
        return ", ".join(roles) if roles else "—"


@admin.register(ContentSample)
class ContentSampleAdmin(EntityModelAdmin):
    list_display = ("name", "kind", "node", "user", "created_at")
    readonly_fields = ("created_at", "name", "user", "image_preview")

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "from-clipboard/",
                self.admin_site.admin_view(self.add_from_clipboard),
                name="nodes_contentsample_from_clipboard",
            ),
            path(
                "capture/",
                self.admin_site.admin_view(self.capture_now),
                name="nodes_contentsample_capture",
            ),
        ]
        return custom + urls

    def add_from_clipboard(self, request):
        try:
            content = pyperclip.paste()
        except PyperclipException as exc:  # pragma: no cover - depends on OS clipboard
            self.message_user(request, f"Clipboard error: {exc}", level=messages.ERROR)
            return redirect("..")
        if not content:
            self.message_user(request, "Clipboard is empty.", level=messages.INFO)
            return redirect("..")
        if ContentSample.objects.filter(
            content=content, kind=ContentSample.TEXT
        ).exists():
            self.message_user(
                request, "Duplicate sample not created.", level=messages.INFO
            )
            return redirect("..")
        user = request.user if request.user.is_authenticated else None
        ContentSample.objects.create(
            content=content, user=user, kind=ContentSample.TEXT
        )
        self.message_user(
            request, "Text sample added from clipboard.", level=messages.SUCCESS
        )
        return redirect("..")

    def capture_now(self, request):
        node = Node.get_local()
        url = request.build_absolute_uri("/")
        try:
            path = capture_screenshot(url)
        except Exception as exc:  # pragma: no cover - depends on selenium setup
            self.message_user(request, str(exc), level=messages.ERROR)
            return redirect("..")
        sample = save_screenshot(path, node=node, method="ADMIN")
        if sample:
            self.message_user(request, f"Screenshot saved to {path}", messages.SUCCESS)
        else:
            self.message_user(request, "Duplicate screenshot; not saved", messages.INFO)
        return redirect("..")

    @admin.display(description="Screenshot")
    def image_preview(self, obj):
        if not obj or obj.kind != ContentSample.IMAGE or not obj.path:
            return ""
        file_path = Path(obj.path)
        if not file_path.is_absolute():
            file_path = settings.LOG_DIR / file_path
        if not file_path.exists():
            return "File not found"
        with file_path.open("rb") as f:
            encoded = base64.b64encode(f.read()).decode("ascii")
        return format_html(
            '<img src="data:image/png;base64,{}" style="max-width:100%;" />',
            encoded,
        )


@admin.register(NetMessage)
class NetMessageAdmin(EntityModelAdmin):
    list_display = (
        "subject",
        "body",
        "reach",
        "node_origin",
        "created",
        "complete",
    )
    search_fields = ("subject", "body")
    list_filter = ("complete", "reach")
    ordering = ("-created",)
    readonly_fields = ("complete",)
    actions = ["send_messages"]

    def send_messages(self, request, queryset):
        for msg in queryset:
            msg.propagate()
        self.message_user(request, f"{queryset.count()} messages sent")

    send_messages.short_description = "Send selected messages"
