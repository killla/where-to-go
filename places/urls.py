from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('places/<int:pk>/', views.place_by_id),
    path('', views.main_page),
]
