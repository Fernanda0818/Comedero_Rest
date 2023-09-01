from django.urls import path
from apps.Mascota.api import mascota_api_view, mascotas_detail_api_view

urlpatterns = [
    path('mascota/', mascota_api_view, name='mascota_api'),
    path('mascota/<int:pk>', mascotas_detail_api_view, name='mascotas_detail_api_view'),
]