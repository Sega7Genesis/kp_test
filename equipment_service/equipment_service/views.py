from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict
from django.shortcuts import get_object_or_404

import requests
import os

from .models import EquipmentModel, Equipment
from .enum import EquipmentState
from .serializers import EquipmentModelSerializer, EquipmentSerializer


#SESSION_SERVICE_URL = os.environ.get("SESSION_SERVICE_URL", "http://enine-session-service.herokuapp.com")  # 'http://127.0.0.1:8300'
SESSION_SERVICE_URL = os.environ.get("SESSION_SERVICE_URL", "https://volosatov-equipment.herokuapp.com/")

class EquipmentView(APIView):
    def post(self, request):
        json_data = request.data
        if isinstance(json_data, QueryDict):
            json_data = json_data.dict()

        serializer = EquipmentSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            equipment = serializer.save()
            return Response(equipment, status=201)
        return Response(status=400)


class SingleEquipmentView(APIView):

    def get(self, request, equipment_uid):
        equipment = get_object_or_404(Equipment, equipment_uid=equipment_uid)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)


class ActivateEquipmentView(APIView):

    def patch(self, request, equipment_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Jwt')
            }
        login_check = requests.get(f"{SESSION_SERVICE_URL}/api/v1/users/login", headers=headers)
        if login_check.status_code != 200:
            return Response({'message': 'Unauthorized'}, status=401)

        equipment = get_object_or_404(Equipment, equipment_uid=equipment_uid)

        if login_check.headers['Admin'] == 'False':
            return Response({'message': 'Forbidden'}, status=403)

        equipment.status = EquipmentState.activate.status
        equipment.save()
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=201)


class DeactivateEquipmentView(APIView):

    def patch(self, request, equipment_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Jwt')
            }
        login_check = requests.get(f"{SESSION_SERVICE_URL}/api/v1/users/login", headers=headers)
        if login_check.status_code != 200:
            return Response({'message': 'Unauthorized'}, status=401)

        equipment = get_object_or_404(Equipment, equipment_uid=equipment_uid)

        if login_check.headers['Admin'] == 'False':
            return Response({'message': 'Forbidden'}, status=403)

        equipment.status = EquipmentState.deactivate.status
        equipment.save()
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=201)


class RemoveEquipmentView(APIView):

    def patch(self, request, equipment_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Jwt')
            }
        login_check = requests.get(f"{SESSION_SERVICE_URL}/api/v1/users/login", headers=headers)
        if login_check.status_code != 200:
            return Response({'message': 'Unauthorized'}, status=401)

        equipment = get_object_or_404(Equipment, equipment_uid=equipment_uid)

        if login_check.headers['Admin'] == 'False':
            return Response({'message': 'Forbidden'}, status=403)

        equipment.status = EquipmentState.remove.status
        equipment.save()
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=201)


class EquipmentModelsView(APIView):

    def post(self, request):
        json_data = request.data
        if isinstance(json_data, QueryDict):
            json_data = json_data.dict()

        serializer = EquipmentModelSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            equipment_model = serializer.save()
            return Response(equipment_model, status=201)
        return Response(status=400)


class SingleEquipmentModelView(APIView):

    def get(self, request, equipment_model_uid):
        equipment_model = get_object_or_404(EquipmentModel, equipment_uid=equipment_model_uid)
        serializer = EquipmentModelSerializer(equipment_model)
        return Response(serializer.data)
