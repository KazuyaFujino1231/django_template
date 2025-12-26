from django.db import models


class Todo(models.Model):
    """Todo item with title, optional description, and completion flag."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        db_table = "todos"
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["is_done"]),
        ]
