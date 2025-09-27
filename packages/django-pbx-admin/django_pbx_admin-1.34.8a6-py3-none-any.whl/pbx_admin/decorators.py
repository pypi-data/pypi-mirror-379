import uuid
from logging import getLogger
from typing import Any, Callable, TypeVar, cast

from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet

log = getLogger(__name__)

T = TypeVar("T", bound=Callable[[Any, QuerySet], int])


def register(*models, **kwargs):
    from pbx_admin.options import ModelAdmin
    from pbx_admin.sites import AdminSite, site

    def _model_admin_wrapper(admin_class):
        if not models:
            raise ValueError("At least one model must be passed to register.")

        admin_site = kwargs.pop("site", site)

        if not isinstance(admin_site, AdminSite):
            raise ValueError("site must subclass AdminSite")

        if not issubclass(admin_class, ModelAdmin):
            raise ValueError("Wrapped class must subclass ModelAdmin.")

        admin_site.register(models, admin_class=admin_class, **kwargs)

        return admin_class

    return _model_admin_wrapper


def try_cached_as(func: T) -> T:
    def wrapper(obj: Any, queryset: QuerySet) -> int:
        # Generate unique call ID for tracking this specific call flow
        call_id = str(uuid.uuid4())[:8]
        model_name = queryset.model._meta.label if queryset.model else "Unknown"

        log.info(f"[{call_id}] try_cached_as START: func={func.__name__}, model={model_name}")
        log.info(f"[{call_id}] queryset: {queryset}")

        try:
            cached_qs = queryset.cache()  # type: ignore[attr-defined]
            log.info(f"[{call_id}] cached queryset created: {cached_qs}")
            result = func(obj, cached_qs)
            log.info(f"[{call_id}] CACHED result: {result}")
            return result
        except (AttributeError, ImproperlyConfigured) as e:
            log.info(
                f"[{call_id}] Cache not available ({e.__class__.__name__}), using "
                "normal queryset"
            )
            result = func(obj, queryset)
            log.info(f"[{call_id}] NORMAL result: {result}")
            return result
        finally:
            log.info(f"[{call_id}] try_cached_as END")

    return cast(T, wrapper)
