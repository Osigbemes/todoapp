from django.urls import path
from . import views

urlpatterns = [
    path ('index', views.index, name='list'),
    path ('update_task/<int:pk>', views.UpdateTask, name='update_task'),
    path ('delete_task/<int:pk>', views.deleteTask, name='delete'),
]
