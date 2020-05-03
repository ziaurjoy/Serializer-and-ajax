from django.urls import path

from api.views import api_overview, task_list,task_create,task_details,task_update,task_delete

urlpatterns = [
    path('', api_overview, name = 'api-overview'),
    path('create-task/', task_create, name = 'create-task'),
    path('task-list/', task_list, name = 'api-serializer-list'),
    path('task-details/<int:pk>/', task_details, name = 'task-details'),
    path('task-update/<int:pk>/', task_update, name = 'task-update'),
    path('task-delete/<int:pk>/', task_delete, name = 'task-delete'),
]