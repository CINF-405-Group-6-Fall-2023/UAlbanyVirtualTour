# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map_view, name='map'),
    path('building/<slug:building_slug>/', views.get_building_info, name='get_building_info'),
]
