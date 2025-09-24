from utils.sites import get_site
from django.urls import Resolver404, resolve
from django.conf import settings
from pathlib import Path
from types import SimpleNamespace
from nodes.models import Node
from core.models import Reference
from core.reference_utils import filter_visible_references
from .models import Module

_favicon_path = Path(settings.BASE_DIR) / "pages" / "fixtures" / "data" / "favicon.txt"
try:
    _DEFAULT_FAVICON = f"data:image/png;base64,{_favicon_path.read_text().strip()}"
except OSError:
    _DEFAULT_FAVICON = ""


def nav_links(request):
    """Provide navigation links for the current site."""
    site = get_site(request)
    node = Node.get_local()
    role = node.role if node else None
    if role:
        modules = (
            Module.objects.filter(node_role=role, is_deleted=False)
            .select_related("application")
            .prefetch_related("landings")
        )
    else:
        modules = []

    valid_modules = []
    current_module = None
    for module in modules:
        landings = []
        for landing in module.landings.filter(enabled=True):
            try:
                match = resolve(landing.path)
            except Resolver404:
                continue
            view_func = match.func
            requires_login = getattr(view_func, "login_required", False) or hasattr(
                view_func, "login_url"
            )
            staff_only = getattr(view_func, "staff_required", False)
            if requires_login and not request.user.is_authenticated:
                continue
            if staff_only and not request.user.is_staff:
                continue
            landings.append(landing)
        if landings:
            app_name = getattr(module.application, "name", "").lower()
            if app_name == "awg":
                module.menu = "Calculate"
            elif app_name == "man":
                module.menu = "Manuals"
            module.enabled_landings = landings
            valid_modules.append(module)
            if request.path.startswith(module.path):
                if current_module is None or len(module.path) > len(
                    current_module.path
                ):
                    current_module = module

    datasette_lock = Path(settings.BASE_DIR) / "locks" / "datasette.lck"
    if datasette_lock.exists():
        datasette_module = SimpleNamespace(
            menu_label="Data",
            path="/data/",
            enabled_landings=[SimpleNamespace(path="/data/", label="Datasette")],
        )
        valid_modules.append(datasette_module)

    valid_modules.sort(key=lambda m: m.menu_label.lower())

    if current_module and current_module.favicon:
        favicon_url = current_module.favicon.url
    else:
        favicon_url = None
        if site:
            try:
                if site.badge.favicon:
                    favicon_url = site.badge.favicon.url
            except Exception:
                pass
        if not favicon_url:
            favicon_url = _DEFAULT_FAVICON

    header_refs_qs = (
        Reference.objects.filter(show_in_header=True)
        .exclude(value="")
        .prefetch_related("roles", "features", "sites")
    )
    header_references = filter_visible_references(
        header_refs_qs,
        request=request,
        site=site,
        node=node,
    )

    return {
        "nav_modules": valid_modules,
        "favicon_url": favicon_url,
        "header_references": header_references,
    }
