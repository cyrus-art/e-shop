from django.contrib import admin
from django.urls import path, include  # Correctly include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
