from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.users.views import RegisterViewSet, LoginViewSet, LogOutViewSet, HitmanViewSet

register = RegisterViewSet.as_view({
    'post': 'create'
})

login = LoginViewSet.as_view({
    'post': 'create'
})

logout = LogOutViewSet.as_view({
    'post': 'create'
})

hitmen = HitmanViewSet.as_view({
    'get': 'list'
})

hitmen_details = HitmanViewSet.as_view({
    'delete': 'destroy',
    'get': 'retrieve'
})

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('hitmen', hitmen, name='hitmen'),
    path('hitmen/<int:pk>', hitmen_details, name='hitmen-details'),
]
