"""core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import Login, Logout

urlpatterns = [
    # Section Admin Panel
    path('admin/', admin.site.urls),
    # Section Api authentication
    path('authentication/login/', Login.as_view(), name='token_obtain_pair'),
    path('authentication/logout/', Logout.as_view(), name='logout'),
    path('authentication/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    # Section Api users
    path('', include('users.routers')),
]
