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
        queryset = apply_list_logic(self.filter_queryset(self.get_queryset()), request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = apply_detail_logic(self.get_object(), request)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        apply_create_logic(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        apply_update_logic(serializer, request)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


def apply_list_logic(queryset, request):
    """Hook for list-time business logic (e.g., filtering, ordering tweaks)."""
    return queryset


def apply_detail_logic(todo: Todo, request):
    """Hook for detail-time business logic (e.g., access control, masking fields)."""
    return todo


def apply_create_logic(serializer, request):
    """Hook for create-time business logic (e.g., defaults, side effects)."""
    serializer.save()


def apply_update_logic(serializer, request):
    """Hook for update-time business logic (e.g., validation, state transitions)."""
    serializer.save()
