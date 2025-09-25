from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']


# serializers.py
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'task-detail', 'lookup_field': 'pk'}
        }


    class Meta:
        model = Task
        fields = [
            'url',
            'id',
            'title',
            'description',
            'assigned_to',
            'due_date',
            'status',
            'completion_report',
            'worked_hours',
            'created_at',
            'updated_at',
        ]
