from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('users/',include('django.contrib.auth.urls')),
    path('projects/',include('projects.urls')),
    path('',include('main.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
