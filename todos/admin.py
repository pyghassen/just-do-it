from django.contrib import admin

from todos.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
        'created_at',
        'modified_at',
    )

admin.site.register(Task, TaskAdmin)
