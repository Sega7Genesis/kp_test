from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict
from django.shortcuts import get_object_or_404
import uuid
import jwt
import datetime

from .models import User
from .serializers import UserSerializer

JWT_SECRET = 'secret'
JWT_LIFETIME = datetime.timedelta(hours=1)


class LoginView(APIView):

    def post(self, request):
        login, password = request.headers.get("Authorization")
        user = get_object_or_404(User, login=login)
        if user.password == hash_password(password):
            token = jwt.encode({'uuid': str(user.user_uid),
                                'expire_at': str(
                                    (datetime.datetime.now() + JWT_LIFETIME).strftime("%Y-%m-%d %H:%M:%S"))},
                               JWT_SECRET, algorithm="HS256")
            user.current_token = token
            user.save()
            serialized = UserSerializer(user)
            return Response(serialized.data, status=200)
        return Response({"message": "wrong password"}, status=400)


class VerifyView(APIView):

    def post(self, request):
        jwt_token = request.headers.get("Authorization")

        if not jwt_token:
            return Response({'message': 'Unauthorized: no token'}, status=401)
        decoded = jwt.decode(jwt_token, JWT_SECRET, algorithms=["HS256"])

        if datetime.datetime.now() > datetime.datetime.strptime(decoded['expire_at'], "%Y-%m-%d %H:%M:%S"):
            return Response({'message': 'Unauthorized: token expired'}, status=401)

        user = User.objects.all().filter(user_uid=uuid.UUID(decoded['uuid']))[0]
        headers = {'Admin': user.is_admin}
        return Response(status=200, headers=headers)


class UsersView(APIView):

    def get(self, request):
        if request.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        if request.headers.get('Admin') == 'False':
            return Response({'message': 'Forbidden (not admin)'}, status=403)

        json_data = request.data
        if isinstance(json_data, QueryDict):
            json_data = json_data.dict()

        user_uid = uuid.uuid4()
        token = jwt.encode({'uuid': str(user_uid),
                            'expire_at': str((datetime.datetime.now() + JWT_LIFETIME).strftime("%Y-%m-%d %H:%M:%S"))},
                           JWT_SECRET, algorithm="HS256")

        json_data.update({'user_uid': user_uid,
                          'current_token': token})
        serializer = UserSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(status=400)
