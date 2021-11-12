from django.urls import path
from . import views


urlpatterns = [
    path('places/<int:pk>/', views.get_place),
    path('', views.get_map),
]
