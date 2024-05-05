from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/catalog/", include("catalog.urls")),
    path("api/v1/catalog/media/images/", include("catalog.urls")),
]
