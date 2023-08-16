from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    path('create/', views.board_create, name='board_create'),
    path('edit/', views.board_edit, name='board_edit'),
    path('delete/', views.board_delete, name='board_delete'),
]
