from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Serialize Todo model to expose core fields."""

    class Meta:
        model = Todo
        fields = ["id", "title", "description", "is_done", "created_at", "updated_at"]
