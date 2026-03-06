from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('task/add/', views.add_task, name='add_task'),
    path('task/<int:task_id>/complete/', views.mark_completed, name='mark_completed'),
    path('task/<int:task_id>/pending/', views.mark_pending, name='mark_pending'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
]
