from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("accounts/", include("accounts.urls")),

    path("dashboard/delete/<int:file_id>/", views.delete_file, name="delete_file"),

    path("dashboard/summary/<int:file_id>/", views.generate_summary, name="generate_summary"),

    path("dashboard/summaries/", views.summaries, name="summaries"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)