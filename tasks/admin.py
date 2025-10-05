from django.contrib import admin
from .models import PostTask

@admin.register(PostTask)
class PostTaskAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'enabled', 'execution_count', 'created_at')
    list_filter = ('platform', 'enabled', 'created_at')
    search_fields = ('url',)
    actions = ['enable_tasks', 'disable_tasks']

    def enable_tasks(self, request, queryset):
        queryset.update(enabled=True)
    enable_tasks.short_description = "Enable selected tasks"