import random
import uuid

from rest_framework.response import Response
from rest_framework.views import APIView


class EquipmentValueGenerateView(APIView):
    def get(self, request):
        equipment_data = {
            "data_uid": uuid.uuid4(),
            "value": random.randint(0, 12592),
            "param": "voltage"
        }
        return Response(equipment_data, status=200)
