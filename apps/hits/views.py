from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_304_NOT_MODIFIED
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

from apps.hits.status import HIT_CREATE, HIT_UPDATE, HIT_NO_CREATE, HIT_DELETED, NOT_FOUND, SUCCESS, ONLY_MANAGER
from apps.hits.status import HITMAN_CREATE, HITMAN_DELETED, HITMAN_NO_CREATE, HITMAN_UPDATE, AN_ERROR_OCURRED

# Serializadores
from apps.hits.serializers import HitModelSerializer

# Modelos
from apps.hits.models import Hit
from apps.users.models import CustomUser

from apps.hits.exceptions import NotFoundException


class HitsViewSet(ViewSet):
    '''
        Clase en la cual se encuentra la logica del CRUD para los hits.
    '''
    serializer_class = HitModelSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Hit.objects.get(pk=pk)
        except Hit.DoesNotExist:
            raise NotFoundException

    def list(self, request):
        user = CustomUser.objects.get(email=request.user)
        if user.id != 1:
            queryset = Hit.objects.all().filter(owner=user, active=True)
        elif user.user_type == 'hitman':
            queryset = Hit.objects.all().filter(assign_hitmans=user, active=True)
        queryset = Hit.objects.all()
        serializer = HitModelSerializer(queryset, many=True)
        if len(serializer.data) >= 1:
            return Response(data = {'status': HTTP_200_OK, 'data': serializer.data, 'message': SUCCESS}, status=HTTP_200_OK)
        return Response(data = {'status': HTTP_404_NOT_FOUND,'data': None, 'message': NOT_FOUND}, status=HTTP_404_NOT_FOUND)

    def create(self, request):
        user = CustomUser.objects.get(email=request.user)
        if user.user_type == 'hitman':
            return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': None, 'message': ONLY_MANAGER}, status=HTTP_400_BAD_REQUEST)
        json_data = {
            'name': request.data.get('name'), 
            'description': request.data.get('description'), 
            'failed_mission': request.data.get('failed_mission'), 
            'assign_hitmans': request.data.get('assign_hitmans'), 
            'owner': user.id
        }
        serializer = HitModelSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={'status': HTTP_201_CREATED, 'data': serializer.data, 'message': HIT_CREATE}, status=HTTP_201_CREATED)
        return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': serializer.errors, 'message': HIT_NO_CREATE}, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        hit = self.get_object(pk=pk)
        if hit.active == False:
            return Response(data = {'status': HTTP_404_NOT_FOUND,'data': None, 'message': NOT_FOUND}, status=HTTP_404_NOT_FOUND)
        serializer = HitModelSerializer(hit)
        return Response(data = {'status': HTTP_200_OK, 'data': serializer.data, 'message': SUCCESS}, status=HTTP_200_OK)

    def update(self, request, pk=None):
        hit = self.get_object(pk=pk)
        user = CustomUser.objects.get(email=request.user)
        serializer = HitModelSerializer(hit, data=request.data)
        if user.user_type == 'hitman':
            return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': None, 'message': ONLY_MANAGER}, status=HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data= {'message': SUCCESS, 'data': serializer.data, 'status': HTTP_200_OK }, status=HTTP_200_OK)
        else:
            return Response(data={'message': AN_ERROR_OCURRED, 'data': None, 'status': HTTP_304_NOT_MODIFIED }, status=HTTP_304_NOT_MODIFIED)

    def partial_update(self, request, pk=None):
        user = CustomUser.objects.get(email=request.user)
        hit = self.get_object(pk=pk)
        serializer = HitModelSerializer(hit, data=request.data, partial=True)
        if user.user_type == 'hitman':
            return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': None, 'message': ONLY_MANAGER}, status=HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data= {'message': SUCCESS, 'data': serializer.data, 'status': HTTP_200_OK }, status=HTTP_200_OK)
        else:
            return Response(data={'message': AN_ERROR_OCURRED, 'data': None, 'status': HTTP_400_BAD_REQUEST }, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        hit = self.get_object(pk=pk)
        user = CustomUser.objects.get(email=request.user)
        if user.user_type == 'hitman':
            return Response(data={'status': HTTP_400_BAD_REQUEST, 'data': None, 'message': ONLY_MANAGER}, status=HTTP_400_BAD_REQUEST)
        if hit.active == True:
            hit.active = False
            hit.save()
            return Response(data = {'status': HTTP_404_NOT_FOUND,'data': None, 'message': NOT_FOUND}, status=HTTP_404_NOT_FOUND)
        return Response(data = {'status': HTTP_204_NO_CONTENT,'data': None, 'message': NOT_FOUND}, status=HTTP_204_NO_CONTENT)