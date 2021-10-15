from django.db import models


class Documentation(models.Model):
    file_name = models.CharField(max_length=255)
    file_uid = models.UUIDField(unique=True)
    content = models.CharField(max_length=1024)
    equipment_model_uid = models.UUIDField(unique=True)
