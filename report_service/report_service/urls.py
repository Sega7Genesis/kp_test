from django.urls import path

from . import views

urlpatterns = [
    path('/equipment-active', views.ReportByActiveEquipment.as_view(), name='equipment-active'),
    path('/equipment-popular', views.ReportByPopularEquipmentView.as_view(), name='equipment-popular')
]