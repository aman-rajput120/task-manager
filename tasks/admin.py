from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'priority', 'category', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'category']
    search_fields = ['title', 'user__username']
