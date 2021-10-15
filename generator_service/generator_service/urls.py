from django.urls import path

from . import views

urlpatterns = [
    path('equipment-value-generate', views.EquipmentValueGenerateView.as_view(), name='equipment-value-generate'),
]