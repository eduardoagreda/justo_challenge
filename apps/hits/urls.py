from django.urls import path
# from rest_framework.routers import DefaultRouter
from apps.hits.views import HitsViewSet

hits_list = HitsViewSet.as_view({
    'get': 'list'
})

hits_create = HitsViewSet.as_view({
    'post': 'create'
})

hits_details = HitsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('hits', hits_list ,name='hits-list'),
    path('hits/create', hits_create ,name='hits-create'),
    path('hits/<int:pk>', hits_details ,name='hists-details'),
]
