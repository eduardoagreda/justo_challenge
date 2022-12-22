from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField

from apps.users.models import CustomUser


class RegisterModelSerializer(ModelSerializer):
    password = CharField(max_length=128, min_length=8, write_only=True)
            
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'user_type']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginModelSerializer(ModelSerializer):
    password = CharField(max_length=128, min_length=8, write_only=True)
            
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'token']
        read_only_fields = ['token']


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model= CustomUser
        fields= ['first_name', 'last_name', 'email', 'user_type', 'description']