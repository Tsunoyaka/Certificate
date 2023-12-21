from django.urls import path
from .views import ChangePasswordView, DeleteAccountView, RegistrationView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)   




urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete-account'),
]


