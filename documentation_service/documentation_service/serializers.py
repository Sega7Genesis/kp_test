from rest_framework import serializers

from .models import Documentation

class DocumentationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = '__all__'
