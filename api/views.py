"""Views for the Todo API endpoints."""

from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Todo API with explicit action mapping.

    list      -> GET /api/todos/
    create    -> POST /api/todos/
    retrieve  -> GET /api/todos/<id>/
    update    -> PUT/PATCH /api/todos/<id>/
    """

    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        """Return paginated or full list of todos."""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """Return a single todo by id."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Create a new todo item."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """Replace or partially update a todo item."""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """Handle PATCH requests by delegating to update with partial=True."""
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)
