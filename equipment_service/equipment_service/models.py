import uuid

from django.db import models
from .enum import EquipmentState


class ActiveModel(models.Model):
    class Meta:
        abstract = True

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class EquipmentModel(ActiveModel):
    equipment_model_uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial_number = models.CharField(max_length=256)


class Equipment(ActiveModel):
    equipment_uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_uid = models.ForeignKey(EquipmentModel, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=256, choices=EquipmentState.choices(), default=EquipmentState.activate.status
    )
