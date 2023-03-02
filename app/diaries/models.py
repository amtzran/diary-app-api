from django.db import models

from base.models import BaseModel, name_file_avatar


class Diary(BaseModel):
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)
    owner = models.ForeignKey(to='users.User', on_delete=models.CASCADE)


class DiaryContacts(BaseModel):
    diary = models.ForeignKey(to='Diary', on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    contact_email = models.EmailField(blank=True, null=True)
    avatar = models.FileField(upload_to=name_file_avatar, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
