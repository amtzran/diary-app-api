from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_deleted', 'groups', 'user_permissions']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.is_verified = True
        user.save()
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)
        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
