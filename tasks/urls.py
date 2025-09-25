from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    TaskListView,
    TaskUpdateView,
    TaskReportView,
    UserTaskListView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),   # 👈 this exposes user-detail
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/report/', TaskReportView.as_view(), name='task-report'),
    path('users/<int:user_id>/tasks/', UserTaskListView.as_view(), name='user-task-list'),
]
