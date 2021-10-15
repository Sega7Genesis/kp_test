from django.urls import path

from . import views

urlpatterns = [
    path('monitors', views.MonitorsView.as_view(), name='monitors'),
    path('monitor/<uuid:monitor_uid>', views.SingleMonitorView.as_view(), name='single_monitor'),
]
