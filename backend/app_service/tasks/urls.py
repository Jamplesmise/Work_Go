# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet
#
# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('edit/', views.task_edit, name='task_edit'),
    path('delete/', views.task_delete, name='task_delete'),
]
