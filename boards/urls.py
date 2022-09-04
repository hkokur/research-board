from django.urls import path
# Views
from .views import (
    BoardList,
    BoardCreate,
    BoardDetail,
    BoardDelete,
    BoardUpdate,
)

urlpatterns = [
    path("", BoardList.as_view(), name="board-list"),
    path("board/new/", BoardCreate.as_view(), name="board-create"),
    path("board/delete/<uuid:board_uuid>", BoardDelete.as_view(), name="board-delete"),
    # format is type:variable name
    path("board/<slug:board_slug>-<uuid:board_uuid>", BoardDetail.as_view(), name="board-detail"),
    path("board/update/<slug:board_slug>-<uuid:board_uuid>", BoardUpdate.as_view(), name="board-update"),
]


