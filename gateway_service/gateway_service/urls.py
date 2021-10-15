from django.urls import path

from . import views

urlpatterns = [
    path('equipment-model', views.EquipmentModelsView.as_view(), name='equipment-model'),
    path('equipment', views.EquipmentView.as_view(), name='equipment'),
    path('equipment/<uuid:equipment_uid>/activate', views.ActivateEquipmentView.as_view(), name='activate_equipment'),
    path('equipment/<uuid:equipment_uid>/deactivate', views.DeactivateEquipmentView.as_view(), name='deactivate_equipment'),
    path('equipment/<uuid:equipment_uid>/remove', views.RemoveEquipmentView.as_view(), name='remove_equipment'),
    path('equipment-model/<uuid:equipment_model_uid>', views.SingleEquipmentModelView.as_view(), name='single_equipment_model'),
    path('equipment/<uuid:equipment_uid>', views.SingleEquipmentView.as_view(), name='single_equipment'),
    path('monitors', views.MonitorsView.as_view(), name='monitors'),
    path('monitor/<uuid:monitor_uid>', views.SingleMonitorView.as_view(), name='single_monitor'),
]
