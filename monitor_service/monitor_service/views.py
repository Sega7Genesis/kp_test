from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict
from django.shortcuts import get_object_or_404

import requests
import os

from .models import Monitor
from .serializers import MonitorModelSerializer


SESSION_SERVICE_URL = os.environ.get("SESSION_SERVICE_URL", "http://127.0.0.1:8300")
EQUIPMENT_SERVICE_URL = os.environ.get("EQUIPMENT_SERVICE_URL", "http://127.0.0.1:8400")
DOCUMENTATION_SERVICE_URL = os.environ.get("DOCUMENTATION_SERVICE_URL", "http://127.0.0.1:8400")

class MonitorsView(APIView):

    def get(self, request):
        monitors = Monitor.objects.all()
        serialized = MonitorModelSerializer(monitors, many=True)
        return Response(serialized.data)

    def post(self, request):
        serializer = MonitorModelSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            monitor = serializer.save()
            return Response(monitor, status=201)
        return Response(status=400)


class SingleMonitorView(APIView):

    def get(self, request, monitor_uid):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Jwt': request.headers.get('Jwt')
        }
        monitor = get_object_or_404(Monitor, equipment_uid=monitor_uid)
        equipment_model_documentation = requests.get(f'{DOCUMENTATION_SERVICE_URL}/api/v1/documentations', headers=headers,
                                                     params={"equipment_models_uid": monitor.equipment_models_uid}).json()
        equipment = requests.get(f'{EQUIPMENT_SERVICE_URL}/api/v1/offices', headers=headers).json()
        serializer = MonitorModelSerializer(monitor)
        return Response(serializer.data)

