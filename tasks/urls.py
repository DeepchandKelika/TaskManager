from django.urls import path
from . import views
from .views import invite_user_view

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('logout/',views.logout_view, name='logout_view'),
    path('create/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('manage_google_keys/', views.manage_google_keys, name='manage_google_keys'),
    path('admin/invite-user/', invite_user_view, name='invite_user'),
]
