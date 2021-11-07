from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.main_page),
    path('places/<int:pk>/', views.place_by_id),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)