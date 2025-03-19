# search_app/urls.py
from django.urls import path
from . import views

app_name = 'search_app'

urlpatterns = [
    path('api/save-search-result/', views.save_search_result, name='save-search-result'),
]