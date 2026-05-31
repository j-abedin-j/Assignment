from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','owner','status','due_date','created_at')
    list_filter = ('owner','status')
    search_fields = ('title','owner','description')