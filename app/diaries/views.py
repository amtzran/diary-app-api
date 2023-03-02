from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from base.pagination import StandardResultsSetPagination
from diaries.serializers import *


class DiaryViewSet(ModelViewSet):
    serializer_class = DiarySerializer
    queryset = Diary.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['owner', 'is_public']
    search_fields = ['name', 'is_public', 'owner__name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DiaryContactViewSet(ModelViewSet):
    serializer_class = DiaryContactSerializer
    queryset = DiaryContacts.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['diary']
    search_fields = ['contact_name', 'contact_phone', 'contact_email', 'diary__name']
