# Generated by Django 3.1.1 on 2021-10-13 22:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentModel',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('equipment_model_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('equipment_uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('activate', 'activate'), ('deactivate', 'deactivate'), ('remove', 'remove')], default='activate', max_length=256)),
                ('model_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment_service.equipmentmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
