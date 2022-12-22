from apps.users.serializers import RegisterModelSerializer
from apps.users.serializers import LoginModelSerializer
from apps.users.serializers import CustomUserModelSerializer

from apps.users.models import CustomUser

from rest_framework.viewsets import ViewSet

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from apps.users.exceptions import NotFoundException

from django.contrib.auth import authenticate, logout

# Constanstes
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from apps.hits.status import HITMAN_CREATE, AN_ERROR_OCURRED, SUCCESS, INVALID_CREDENTIALS, NOT_FOUND, ONLY_MANAGER

class RegisterViewSet(ViewSet):
    
    serializer_class = RegisterModelSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={'status': HTTP_201_CREATED, 'data': serializer.data, 'message':HITMAN_CREATE}, status=HTTP_201_CREATED)
        return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': serializer.errors, 'message':AN_ERROR_OCURRED}, status=HTTP_400_BAD_REQUEST)


class LoginViewSet(ViewSet):
    serializer_class = LoginModelSerializer

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return Response(data={'status': HTTP_200_OK, 'data': serializer.data, 'message': SUCCESS}, status=HTTP_200_OK)
        return Response(data={'status': HTTP_401_UNAUTHORIZED, 'data': None, 'message': INVALID_CREDENTIALS}, status=HTTP_401_UNAUTHORIZED)            


class LogOutViewSet(ViewSet):
    permission_classes = [IsAuthenticated,]

    def create(self, request):
        logout(request)
        return Response(data={'status': HTTP_200_OK, 'data': None, 'message': SUCCESS}, status=HTTP_200_OK)   


class HitmanViewSet(ViewSet):
    serializer_class = CustomUserModelSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise NotFoundException

    def list(self, request):
        user = CustomUser.objects.get(email=request.user)

        if user.id == 1:
            users = CustomUser.objects.all()
            serializer = self.serializer_class(users, many=True)
            if len(serializer.data) >= 1:
                return Response(data = {'status': HTTP_200_OK, 'data': serializer.data, 'message': SUCCESS}, status=HTTP_200_OK)
            return Response(data = {'status': HTTP_404_NOT_FOUND,'data': None, 'message': NOT_FOUND}, status=HTTP_404_NOT_FOUND)
        elif user.user_type == 'manager':
            users = CustomUser.objects.all()
            serializer = self.serializer_class(users, many=True)
            if len(serializer.data) >= 1:
                return Response(data = {'status': HTTP_200_OK, 'data': serializer.data, 'message': SUCCESS}, status=HTTP_200_OK)
            return Response(data = {'status': HTTP_404_NOT_FOUND,'data': None, 'message': NOT_FOUND}, status=HTTP_404_NOT_FOUND)
        return Response(data = {'status': HTTP_400_BAD_REQUEST,'data': None, 'message': AN_ERROR_OCURRED}, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        hitman = self.get_object(pk=pk)
        if hitman.user_type == 'hitman':
            return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': None, 'message': ONLY_MANAGER}, status=HTTP_400_BAD_REQUEST)
        if hitman.active == False and hitman.is_active == False:
            return Response(data = {'status': HTTP_404_NOT_FOUND,'data': None, 'message': NOT_FOUND}, status=HTTP_404_NOT_FOUND)
        serializer = CustomUserModelSerializer(hitman)
        return Response(data = {'status': HTTP_200_OK, 'data': serializer.data, 'message': SUCCESS}, status=HTTP_200_OK)


    def destroy(self, request, pk=None):
        hitman = self.get_object(pk=pk)
        user = CustomUser.objects.get(email=request.user)
        if user.user_type == 'hitman':
            return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': None, 'message': ONLY_MANAGER}, status=HTTP_400_BAD_REQUEST)
        if hitman.active == True and hitman.is_active == True:
            hitman.active = False
            hitman.is_active = False
            hitman.save()
            return Response(data = {'status': HTTP_404_NOT_FOUND,'data': None, 'message': NOT_FOUND}, status=HTTP_404_NOT_FOUND)
        return Response(data = {'status': HTTP_204_NO_CONTENT,'data': None, 'message': NOT_FOUND}, status=HTTP_204_NO_CONTENT)