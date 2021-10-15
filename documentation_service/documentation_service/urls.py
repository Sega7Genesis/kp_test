from django.urls import path

from . import views

urlpatterns = [
    path('documentations', views.DocumentationByEquipmentModelView.as_view(), name='documentations')
]