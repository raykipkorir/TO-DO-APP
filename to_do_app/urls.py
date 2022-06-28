from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_tasks,name = "tasks"),
    path('update_task/<pk>/',views.update_task,name = "update_task"),
    path('delete_task/<pk>/',views.delete_task,name = "delete_task"),

]
