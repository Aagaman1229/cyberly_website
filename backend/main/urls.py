# urls.py

# backend/urls.py or your project-level urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import article

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('article/',article)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
