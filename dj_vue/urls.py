from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from api.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
