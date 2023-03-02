from rest_framework import serializers

from diaries.models import Diary, DiaryContacts
from users.serializers import *


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        exclude = ['is_deleted', 'deleted_at', 'owner']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['owner'] = UserSerializer(instance.owner).data
        return data


class DiaryBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        exclude = ['is_deleted', 'deleted_at']


class DiaryContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryContacts
        exclude = ['is_deleted', 'deleted_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['diary'] = DiaryBasicSerializer(instance.diary).data
        return data
