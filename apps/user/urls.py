from django.urls import path
from apps.user.views import index

urlpatterns = [
    path('api/v0.1/assassins', index ,name='assassins-list')
]
