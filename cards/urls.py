from django.urls import path
# Views
from .views import (
    UrlCardCreate,
    UrlCardUpdate,
    UrlCardDelete,
    UrlCreate,
    UrlDelete
)

urlpatterns = [
    # get board uuid to add board
    path("urlcard/new/<uuid:board_uuid>/", UrlCardCreate.as_view(), name="urlcard-create"),
    # update and also detail view
    path("urlcard/<slug:urlcard_slug>-<uuid:urlcard_uuid>/", UrlCardUpdate.as_view(), name="urlcard-update"),
    # delete url card
    path("urlcard/delete/<uuid:urlcard_uuid>/", UrlCardDelete.as_view(), name="urlcard-delete"),

    # get uuid to create relationships with UrlCard
    path("url/new/<uuid:urlcard_uuid>/", UrlCreate.as_view(), name="url-create"),
    # delete url 
    path("url/delete/<uuid:url_uuid>/", UrlDelete.as_view(), name="url-delete"),
]