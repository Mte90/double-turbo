from django.contrib import admin
from django.urls import include, path
from turbodrf.router import TurboDRFRouter
from turbodrf.documentation import get_turbodrf_schema_view

schema_view = get_turbodrf_schema_view()

from .api import UserViewSet

router = TurboDRFRouter()
router.register("users", UserViewSet, basename="user-model")

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("stripe/", include("drf_stripe.urls")),
    path('', include('django_prometheus.urls')),
    path('auth/', include('dj_rest_auth.urls')),

    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
