from rest_framework import serializers

from .models import Monitor


class MonitorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'
