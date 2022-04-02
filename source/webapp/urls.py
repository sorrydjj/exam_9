from django.urls import path

from webapp.views.photo import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, PhotoTokenView
from webapp.views.album import AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

from webapp.views.favorite import PhotoAddFavoriteView, PhotoDeleteFavoriteView

app_name = "webapp"

urlpatterns = [
    path("gallery/", PhotoListView.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name="photo_detail"),
    path("photo/create/", PhotoCreateView.as_view(), name="photo_create"),
    path("photo/update/<int:pk>/", PhotoUpdateView.as_view(), name="photo_update"),
    path("photo/delete/<int:pk>/", PhotoDeleteView.as_view(), name="photo_delete"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("album/create/", AlbumCreateView.as_view(), name="album_create"),
    path("album/update/<int:pk>/", AlbumUpdateView.as_view(), name="album_update"),
    path("album/delete/<int:pk>/", AlbumDeleteView.as_view(), name="album_delete"),
    path("<token>/", PhotoTokenView.as_view(), name="token_view"),
    path("favorit/photo/add/<int:pk>/", PhotoAddFavoriteView.as_view(), name="favorite_photo_add"),
    path("favorit/photo/delete/<int:pk>", PhotoDeleteView.as_view(), name="favorite_photo_delete")
]
