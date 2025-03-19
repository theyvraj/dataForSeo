# project/urls.py (your main project urls file)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('saveJson.urls', namespace='search')),
]