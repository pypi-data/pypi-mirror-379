from django.contrib import admin, messages
from django import forms

import asyncio
from datetime import timedelta
import json

from django.shortcuts import redirect
from django.utils import timezone
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse

from .models import (
    Charger,
    Simulator,
    MeterValue,
    Transaction,
    Location,
)
from .simulator import ChargePointSimulator
from . import store
from .transactions_io import (
    export_transactions,
    import_transactions as import_transactions_data,
)
from core.user_data import EntityModelAdmin


class LocationAdminForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

        widgets = {
            "latitude": forms.NumberInput(attrs={"step": "any"}),
            "longitude": forms.NumberInput(attrs={"step": "any"}),
        }

    class Media:
        css = {"all": ("https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",)}
        js = (
            "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js",
            "ocpp/charger_map.js",
        )


class TransactionExportForm(forms.Form):
    start = forms.DateTimeField(required=False)
    end = forms.DateTimeField(required=False)
    chargers = forms.ModelMultipleChoiceField(
        queryset=Charger.objects.all(), required=False
    )


class TransactionImportForm(forms.Form):
    file = forms.FileField()


class LogViewAdminMixin:
    """Mixin providing an admin view to display charger or simulator logs."""

    log_type = "charger"
    log_template_name = "admin/ocpp/log_view.html"

    def get_log_identifier(self, obj):  # pragma: no cover - mixin hook
        raise NotImplementedError

    def get_log_title(self, obj):
        return f"Log for {obj}"

    def get_urls(self):
        urls = super().get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        custom = [
            path(
                "<path:object_id>/log/",
                self.admin_site.admin_view(self.log_view),
                name=f"{info[0]}_{info[1]}_log",
            ),
        ]
        return custom + urls

    def log_view(self, request, object_id):
        obj = self.get_object(request, object_id)
        if obj is None:
            self.message_user(request, "Log is not available.", messages.ERROR)
            return redirect("..")
        identifier = self.get_log_identifier(obj)
        log_entries = store.get_logs(identifier, log_type=self.log_type)
        log_file = store._file_path(identifier, log_type=self.log_type)
        context = {
            **self.admin_site.each_context(request),
            "opts": self.model._meta,
            "original": obj,
            "title": self.get_log_title(obj),
            "log_entries": log_entries,
            "log_file": str(log_file),
            "log_identifier": identifier,
        }
        return TemplateResponse(request, self.log_template_name, context)


@admin.register(Location)
class LocationAdmin(EntityModelAdmin):
    form = LocationAdminForm
    list_display = ("name", "latitude", "longitude")
    change_form_template = "admin/ocpp/location/change_form.html"


@admin.register(Charger)
class ChargerAdmin(LogViewAdminMixin, EntityModelAdmin):
    fieldsets = (
        (
            "General",
            {
                "fields": (
                    "charger_id",
                    "display_name",
                    "connector_id",
                    "location",
                    "last_path",
                    "last_heartbeat",
                    "last_meter_values",
                    "firmware_status",
                    "firmware_status_info",
                    "firmware_timestamp",
                )
            },
        ),
        (
            "Diagnostics",
            {
                "fields": (
                    "diagnostics_status",
                    "diagnostics_timestamp",
                    "diagnostics_location",
                )
            },
        ),
        (
            "Configuration",
            {"fields": ("public_display", "require_rfid")},
        ),
        (
            "References",
            {
                "fields": ("reference",),
            },
        ),
    )
    readonly_fields = (
        "last_heartbeat",
        "last_meter_values",
        "firmware_status",
        "firmware_status_info",
        "firmware_timestamp",
    )
    list_display = (
        "charger_id",
        "connector_id",
        "location_name",
        "require_rfid_display",
        "public_display",
        "last_heartbeat",
        "firmware_status",
        "firmware_timestamp",
        "session_kw",
        "total_kw_display",
        "page_link",
        "log_link",
        "status_link",
    )
    search_fields = ("charger_id", "connector_id", "location__name")
    actions = ["purge_data", "delete_selected"]

    def get_view_on_site_url(self, obj=None):
        return obj.get_absolute_url() if obj else None

    def require_rfid_display(self, obj):
        return obj.require_rfid

    require_rfid_display.boolean = True
    require_rfid_display.short_description = "RFID Auth"

    def page_link(self, obj):
        from django.utils.html import format_html

        return format_html(
            '<a href="{}" target="_blank">open</a>', obj.get_absolute_url()
        )

    page_link.short_description = "Landing"

    def qr_link(self, obj):
        from django.utils.html import format_html

        if obj.reference and obj.reference.image:
            return format_html(
                '<a href="{}" target="_blank">qr</a>', obj.reference.image.url
            )
        return ""

    qr_link.short_description = "QR Code"

    def log_link(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse

        url = reverse("admin:ocpp_charger_log", args=[obj.pk])
        return format_html('<a href="{}" target="_blank">view</a>', url)

    log_link.short_description = "Log"

    def get_log_identifier(self, obj):
        return store.identity_key(obj.charger_id, obj.connector_id)

    def status_link(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse

        url = reverse(
            "charger-status-connector",
            args=[obj.charger_id, obj.connector_slug],
        )
        return format_html('<a href="{}" target="_blank">status</a>', url)

    status_link.short_description = "Status"

    def location_name(self, obj):
        return obj.location.name if obj.location else ""

    location_name.short_description = "Location"

    def purge_data(self, request, queryset):
        for charger in queryset:
            charger.purge()
        self.message_user(request, "Data purged for selected chargers")

    purge_data.short_description = "Purge data"

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

    def total_kw_display(self, obj):
        return round(obj.total_kw, 2)

    total_kw_display.short_description = "Total kW"

    def session_kw(self, obj):
        tx = store.get_transaction(obj.charger_id, obj.connector_id)
        if tx:
            return round(tx.kw, 2)
        return 0.0

    session_kw.short_description = "Session kW"


@admin.register(Simulator)
class SimulatorAdmin(LogViewAdminMixin, EntityModelAdmin):
    list_display = (
        "name",
        "cp_path",
        "host",
        "ws_port",
        "ws_url",
        "interval",
        "kw_max",
        "running",
        "log_link",
    )
    fields = (
        "name",
        "cp_path",
        ("host", "ws_port"),
        "rfid",
        ("duration", "interval", "pre_charge_delay"),
        "kw_max",
        ("repeat", "door_open"),
        ("username", "password"),
    )
    actions = ("start_simulator", "stop_simulator", "send_open_door")

    log_type = "simulator"

    def save_model(self, request, obj, form, change):
        previous_door_open = False
        if change and obj.pk:
            previous_door_open = (
                type(obj)
                .objects.filter(pk=obj.pk)
                .values_list("door_open", flat=True)
                .first()
                or False
            )
        super().save_model(request, obj, form, change)
        if obj.door_open and not previous_door_open:
            triggered = self._queue_door_open(request, obj)
            if not triggered:
                type(obj).objects.filter(pk=obj.pk).update(door_open=False)
                obj.door_open = False

    def _queue_door_open(self, request, obj) -> bool:
        sim = store.simulators.get(obj.pk)
        if not sim:
            self.message_user(
                request,
                f"{obj.name}: simulator is not running",
                level=messages.ERROR,
            )
            return False
        type(obj).objects.filter(pk=obj.pk).update(door_open=True)
        obj.door_open = True
        store.add_log(
            obj.cp_path,
            "Door open event requested from admin",
            log_type="simulator",
        )
        if hasattr(sim, "trigger_door_open"):
            sim.trigger_door_open()
        else:  # pragma: no cover - unexpected condition
            self.message_user(
                request,
                f"{obj.name}: simulator cannot send door open event",
                level=messages.ERROR,
            )
            type(obj).objects.filter(pk=obj.pk).update(door_open=False)
            obj.door_open = False
            return False
        type(obj).objects.filter(pk=obj.pk).update(door_open=False)
        obj.door_open = False
        self.message_user(
            request,
            f"{obj.name}: DoorOpen status notification sent",
        )
        return True

    def running(self, obj):
        return obj.pk in store.simulators

    running.boolean = True

    @admin.action(description="Send Open Door")
    def send_open_door(self, request, queryset):
        for obj in queryset:
            self._queue_door_open(request, obj)

    def start_simulator(self, request, queryset):
        from django.urls import reverse
        from django.utils.html import format_html

        for obj in queryset:
            if obj.pk in store.simulators:
                self.message_user(request, f"{obj.name}: already running")
                continue
            type(obj).objects.filter(pk=obj.pk).update(door_open=False)
            obj.door_open = False
            store.register_log_name(obj.cp_path, obj.name, log_type="simulator")
            sim = ChargePointSimulator(obj.as_config())
            started, status, log_file = sim.start()
            if started:
                store.simulators[obj.pk] = sim
            log_url = reverse("admin:ocpp_simulator_log", args=[obj.pk])
            self.message_user(
                request,
                format_html(
                    '{}: {}. Log: <code>{}</code> (<a href="{}" target="_blank">View Log</a>)',
                    obj.name,
                    status,
                    log_file,
                    log_url,
                ),
            )

    start_simulator.short_description = "Start selected simulators"

    def stop_simulator(self, request, queryset):
        async def _stop(objs):
            for obj in objs:
                sim = store.simulators.pop(obj.pk, None)
                if sim:
                    await sim.stop()

        asyncio.get_event_loop().create_task(_stop(list(queryset)))
        self.message_user(request, "Stopping simulators")

    stop_simulator.short_description = "Stop selected simulators"

    def log_link(self, obj):
        from django.utils.html import format_html
        from django.urls import reverse

        url = reverse("admin:ocpp_simulator_log", args=[obj.pk])
        return format_html('<a href="{}" target="_blank">view</a>', url)

    log_link.short_description = "Log"

    def get_log_identifier(self, obj):
        return obj.cp_path


class MeterValueInline(admin.TabularInline):
    model = MeterValue
    extra = 0
    fields = (
        "timestamp",
        "context",
        "energy",
        "voltage",
        "current_import",
        "current_offered",
        "temperature",
        "soc",
        "connector_id",
    )
    readonly_fields = fields
    can_delete = False


@admin.register(Transaction)
class TransactionAdmin(EntityModelAdmin):
    change_list_template = "admin/ocpp/transaction/change_list.html"
    list_display = (
        "charger",
        "account",
        "rfid",
        "meter_start",
        "meter_stop",
        "start_time",
        "stop_time",
        "kw",
    )
    readonly_fields = ("kw",)
    list_filter = ("charger", "account")
    date_hierarchy = "start_time"
    inlines = [MeterValueInline]

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "export/",
                self.admin_site.admin_view(self.export_view),
                name="ocpp_transaction_export",
            ),
            path(
                "import/",
                self.admin_site.admin_view(self.import_view),
                name="ocpp_transaction_import",
            ),
        ]
        return custom + urls

    def export_view(self, request):
        if request.method == "POST":
            form = TransactionExportForm(request.POST)
            if form.is_valid():
                chargers = form.cleaned_data["chargers"]
                data = export_transactions(
                    start=form.cleaned_data["start"],
                    end=form.cleaned_data["end"],
                    chargers=[c.charger_id for c in chargers] if chargers else None,
                )
                response = HttpResponse(
                    json.dumps(data, indent=2, ensure_ascii=False),
                    content_type="application/json",
                )
                response["Content-Disposition"] = (
                    "attachment; filename=transactions.json"
                )
                return response
        else:
            form = TransactionExportForm()
        context = self.admin_site.each_context(request)
        context["form"] = form
        return TemplateResponse(request, "admin/ocpp/transaction/export.html", context)

    def import_view(self, request):
        if request.method == "POST":
            form = TransactionImportForm(request.POST, request.FILES)
            if form.is_valid():
                data = json.load(form.cleaned_data["file"])
                imported = import_transactions_data(data)
                self.message_user(request, f"Imported {imported} transactions")
                return HttpResponseRedirect("../")
        else:
            form = TransactionImportForm()
        context = self.admin_site.each_context(request)
        context["form"] = form
        return TemplateResponse(request, "admin/ocpp/transaction/import.html", context)


class MeterValueDateFilter(admin.SimpleListFilter):
    title = "Timestamp"
    parameter_name = "timestamp_range"

    def lookups(self, request, model_admin):
        return [
            ("today", "Today"),
            ("7days", "Last 7 days"),
            ("30days", "Last 30 days"),
            ("older", "Older than 30 days"),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        now = timezone.now()
        if value == "today":
            start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end = start + timedelta(days=1)
            return queryset.filter(timestamp__gte=start, timestamp__lt=end)
        if value == "7days":
            start = now - timedelta(days=7)
            return queryset.filter(timestamp__gte=start)
        if value == "30days":
            start = now - timedelta(days=30)
            return queryset.filter(timestamp__gte=start)
        if value == "older":
            cutoff = now - timedelta(days=30)
            return queryset.filter(timestamp__lt=cutoff)
        return queryset


@admin.register(MeterValue)
class MeterValueAdmin(EntityModelAdmin):
    list_display = (
        "charger",
        "timestamp",
        "context",
        "energy",
        "voltage",
        "current_import",
        "current_offered",
        "temperature",
        "soc",
        "connector_id",
        "transaction",
    )
    date_hierarchy = "timestamp"
    list_filter = ("charger", MeterValueDateFilter)
