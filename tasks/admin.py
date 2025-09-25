from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User, Task

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    fieldsets = DefaultUserAdmin.fieldsets + ((None, {'fields': ('role','assigned_admin')}),)
    add_fieldsets = DefaultUserAdmin.add_fieldsets + ((None, {'fields': ('role','assigned_admin')}),)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'due_date', 'worked_hours')
    list_filter = ('status', 'due_date')
    search_fields = ('title','description','assigned_to__username')
