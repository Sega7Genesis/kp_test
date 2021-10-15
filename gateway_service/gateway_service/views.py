from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import datetime
import os
import ast

from .forms import (
    LoginForm,
    RegisterForm,
    CarForm,
    OfficeForm,
    CarInOfficeForm,
    PaymentForm,
    NewBookingForm,
    CarsFilterForm
)


EQUIPMENT_SERVICE_URL = os.environ.get("EQUIPMENT_SERVICE_URL", "http://127.0.0.1:8500")
MONITOR_SERVICE_URL = os.environ.get("MONITOR_SERVICE_URL", "http://127.0.0.1:8501")  # 'http://127.0.0.1:8100'
SESSION_SERVICE_URL = os.environ.get("SESSION_SERVICE_URL", "https://volosatov-session.herokuapp.com/")  # 'http://127.0.0.1:8300'
REPORT_SERVICE_URL = os.environ.get("REPORT_SERVICE_URL", " https://volosatov-report.herokuapp.com/")  # 'http://127.0.0.1:8400'


class EquipmentModelsView(APIView):

    def post(self, request):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        if response_check_jwt.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        response_equipment_model = requests.get(f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment-model", headers=headers)
        return response_equipment_model


class EquipmentView(APIView):

    def post(self, request):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        if response_check_jwt.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        response_equipment= requests.get(f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment", headers=headers)
        return response_equipment


class ActivateEquipmentView(APIView):

    def patch(self, request, equipment_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        if response_check_jwt.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        response_activate_equipment = requests.get(f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment/{equipment_uid}/activate", headers=headers)
        return response_activate_equipment


class DeactivateEquipmentView(APIView):

    def patch(self, request, equipment_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        if response_check_jwt.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        response_deactivate_equipment = requests.get(f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment/{equipment_uid}/deactivate",
                                                   headers=headers)
        return response_deactivate_equipment


class RemoveEquipmentView(APIView):

    def patch(self, request, equipment_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        if response_check_jwt.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        response_remove_equipment = requests.get(
            f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment/{equipment_uid}/remove",
            headers=headers)
        return response_remove_equipment


class SingleEquipmentModelView(APIView):

    def get(self, request, equipment_model_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        response_equipment_model = requests.get(
            f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment-model/{equipment_model_uid}",
            headers=headers)
        return response_equipment_model


class SingleEquipmentView(APIView):

    def get(self, request, equipment_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        response_equipment_model = requests.get(
            f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment/{equipment_model_uid}",
            headers=headers)
        return response_equipment_model


class MonitorsView(APIView):

    def get(self, request):
        response_monitor = requests.get(
            f"{MONITOR_SERVICE_URL}/api/v1/monitors")
        return response_monitor

    def post(self, request):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Jwt')
        }
        login_check = requests.get(f"{SESSION_SERVICE_URL}/api/v1/users/login", headers=headers)
        if login_check.status_code != 200:
            return Response({'message': 'Unauthorized'}, status=401)

        json_data = request.data
        if isinstance(json_data, QueryDict):
            json_data = json_data.dict()

        serializer = MonitorModelSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            monitor = serializer.save()
            return Response(monitor, status=201)
        return Response(status=400)


class SingleMonitorView(APIView):

    def get(self, request, monitor_uid):
        response_monitor = requests.get(
            f"{MONITOR_SERVICE_URL}/api/v1/monitors/{monitor_uid}")
        return response_monitor


class ReportByActiveEquipment(APIView):
    def get(self, request):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Authorization')
        }
        response_check_jwt = requests.get(f"{SESSION_SERVICE_URL}/api/v1/verify", headers=headers)
        if response_check_jwt.status_code != 200:
            return response_check_jwt

        if response_check_jwt.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        active_equipment_report = requests.get(f"{REPORT_SERVICE_URL}/api/v1/equipment", headers=headers)
        active_count = 0
        for equipment in equipments:
            if equipment.status != "active":
                continue
            active_count += 1

        Response({"count_of_active_equipment": active_count}, status=200)

