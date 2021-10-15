from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Documentation
from .serializers import DocumentationModelSerializer


class DocumentationByEquipmentModelView(APIView):
    def get(self, request):
        equipments_model_uid = request.params.get("equipments_model_uid")
        if equipments_model_uid:
            documentations = Documentation.objects.filter(equipment_model_uid=equipments_model_uid)
        else:
            documentations = Documentation.objects.all()
        serializer = DocumentationModelSerializer(documentations, many=True)
        return Response(serializer.data)
