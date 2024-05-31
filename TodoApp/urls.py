from django.urls import path
from . import views

urlpatterns = [
    path('view', views.Todo_view, name='home' ),
    path('add_task', views.add_task, name='add_task'),
    path('task_done/<int:id>/',views.task_done, name='task_done'),
     path('del_task/<int:id>/',views.del_task, name='del_task'),
     path('update_task/<int:id>/',views.update_task, name='update_task'),
     path('undo_task/<int:id>/',views.undo_task, name='undo_task'),
]