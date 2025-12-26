from django.contrib import admin

from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """Admin configuration for Todo entries."""

    list_display = ("id", "title", "is_done", "created_at", "updated_at")
    list_filter = ("is_done",)
    search_fields = ("title", "description")
