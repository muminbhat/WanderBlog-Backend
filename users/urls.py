from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('test/', views.testEndPoint, name='test'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]
