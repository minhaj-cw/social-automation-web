from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.DeviceSyncView.as_view()),
    path('tasks/', views.TaskSyncView.as_view()),
    path('results/', views.TaskResultView.as_view()),
]