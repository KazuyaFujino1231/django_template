from django.urls import path

from .views import TodoViewSet

# パスを変えても reverse() / {% url %} を安定させるために必ず name を付ける。
# reverse() はビュー名や name を元にURL文字列を逆引きするので、リンク生成をコードにハードコーディングしない。
urlpatterns = [
    path("todos/", TodoViewSet.as_view({"get": "list", "post": "create"}), name="todo-list-create"),
    path("todos/<int:pk>/", TodoViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update"}), name="todo-detail"),
]
