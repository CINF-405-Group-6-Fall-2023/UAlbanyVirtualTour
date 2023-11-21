# urls.py
from django.urls import path
from .views import get_building_info
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('get_building_info/<slug:building_slug>/', get_building_info, name='get_building_info'),
]
