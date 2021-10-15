import hashlib

from rest_framework import serializers
from .models import User


def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_uid = serializers.UUIDField()
    login = serializers.CharField(max_length=31)
    password = serializers.CharField(max_length=50)
    is_admin = serializers.BooleanField()
    current_token = serializers.CharField(max_length=255)

    def create(self, validated_data):
        validated_data['password'] = hash_password(validated_data['password'])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if (password := validated_data.get('password')) is not None:
            instance.password = hash_password(password)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.save()
        return instance

    def validate(self, data):
        return data
