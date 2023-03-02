from rest_framework import routers

from diaries.views import *

router = routers.SimpleRouter()
router.register(r'diaries', DiaryViewSet, basename='diaries')
router.register(r'diary-contacts', DiaryContactViewSet, basename='diary-contacts')

urlpatterns = router.urls
