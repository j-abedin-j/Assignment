from django.urls import path
from . import views

urlpatterns = [
    path('',                     views.home,        name='home'),
    path('register/',            views.register,    name='register'),
    path('tasks/',               views.task_list,   name='task_list'),
    path('create/',              views.task_form,   name='task_form'),
    path('update/<int:pk>/',     views.task_update, name='task_update'),
    path('delete/<int:pk>/',     views.task_delete, name='task_delete'),
]