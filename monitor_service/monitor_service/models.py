import uuid

from django.db import models


class Monitor(models.Model):
    monitor_uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    equipment_uid = models.UUIDField(editable=False)
    equipment_models_uid = models.UUIDField(editable=False)
