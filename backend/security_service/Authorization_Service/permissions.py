from rest_framework import permissions
import jwt

class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token:
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                # 可以添加更多的验证逻辑，如检查用户是否存在
                return True
            except:
                pass
        return False
# Compare this snippet from backend\security_service\Authorization_Service\views.py:
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Permission
# from .serializers import PermissionSerializer
#
# class PermissionViewSet(viewsets.ModelViewSet):
#     queryset = Permission.objects.all()
#     serializer_class = PermissionSerializer
#
# class PermissionView(APIView):
#     def get(self, request):
#         # 获取用户的权限列表
#         pass
#
#     def post(self, request):
#         # 为用户添加权限
#         pass
#
#     def delete(self, request):
#         # 为用户删除权限
#         pass
# Compare this snippet from backend\security_service\Authentication_Service\urls.py:
# from django.urls import path
# from .views import LoginView, RegisterView
#
# urlpatterns = [
#     path('login/', LoginView.as_view()),
#     path('register/', RegisterView.as_view()),
# ]
# Compare this snippet from backend\security_service\Authorization_Service\urls.py:
# from django.urls import path
# from .views import PermissionViewSet, PermissionView
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('permissions', PermissionViewSet, basename='permissions')
#
# urlpatterns = [
#     path('user_permissions/', PermissionView.as_view()),
# ]
# Compare this snippet from backend\security_service\Authentication_Service\serializers.py:
# from rest_framework import serializers
# from django.contrib.auth.models import User
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
# Compare this snippet from backend\security_service\Authorization_Service\serializers.py:
# from rest_framework import serializers
# from .models import Permission
#
# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permission
#         fields = ['name', 'description']
# Compare this snippet from backend\security_service\Authentication_Service\models.py:
# from django.db import models
# from django.contrib.auth.models import User
#
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.username
# Compare this snippet from backend\security_service\Authorization_Service\models.py:
# from django.db import models
#
# class Permission(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
# Compare this snippet from backend\security_service\Authentication_Service\tests.py:
# from django.test import TestCase
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient
# from rest_framework import status
# import json
#
# class AuthenticationTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='test', email='test@test', password='test')
#
#     def test_register(self):
#         response = self.client.post('/register/', {'username': 'test2', 'email': 'test2@test', 'password': 'test2'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_login(self):
#         pass