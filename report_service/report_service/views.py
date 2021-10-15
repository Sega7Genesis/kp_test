from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import os


EQUIPMENT_SERVICE_URL = os.environ.get("EQUIPMENT_SERVICE_URL", "http://127.0.0.1:8500")
MONITOR_SERVICE_URL = os.environ.get("MONITOR_SERVICE_URL", "http://127.0.0.1:8501")

class ReportByActiveEquipment(APIView):
    def get(self, request):
        equipments = requests.get(f"{EQUIPMENT_SERVICE_URL}/api/v1/equipment", headers=request.headers).json()
        active_count = 0
        for equipment in equipments:
            if equipment.status != "active":
                continue
            active_count += 1

        Response({"count_of_active_equipment": active_count}, status=200)


class ReportByPopularEquipmentView(APIView):
    def get(self, request):
        monitors = requests.get(f"{MONITOR_SERVICE_URL}/api/v1/monitors", headers=request.headers).json()
        popular_stat = dict()
        for monitor in monitors:
            if monitor['equipment_uid'] not in popular_stat:
                popular_stat[monitor['equipment_uid']] = 1
            else:
                popular_stat[monitor['equipment_uid']] += 1
        return Response(popular_stat, status=200)
