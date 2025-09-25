from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model
from .models import Task
from .serializers import TaskSerializer, UserSerializer

User = get_user_model()


# User ViewSet (for Admin/SuperAdmin to browse users)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


# Logged-in user's tasks
class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'superadmin':
            # SuperAdmins see all tasks
            return Task.objects.all()
        elif user.role == 'admin':
            # Admins see tasks assigned to their users
            return Task.objects.filter(assigned_to__assigned_admin=user)
        else:
            # Regular users see only their own tasks
            return Task.objects.filter(assigned_to=user)

# Update a task (mark as completed with report + hours)
class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


# Report view (only Admins & SuperAdmins)
class TaskReportView(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Task.objects.filter(status='completed')

    def get_queryset(self):
        user = self.request.user
        # SuperAdmin sees all completed tasks
        if user.role == 'superadmin':
            return Task.objects.filter(status='completed')
        # Admin sees completed tasks assigned to their users
        elif user.role == 'admin':
            return Task.objects.filter(status='completed', assigned_to__assigned_admin=user)
        # Regular users cannot access
        return Task.objects.none()
# Admin/SuperAdmin: tasks of a specific user
class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_to_id=user_id)
