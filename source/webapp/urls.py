from django.urls import path

from webapp.views.photo import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = "webapp"

urlpatterns = [
    path("gallery/", PhotoListView.as_view(), name="index"),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name="photo_detail"),
    path("photo/create/", PhotoCreateView.as_view(), name="photo_create"),
    path("photo/update/<int:pk>/", PhotoUpdateView.as_view(), name="photo_update"),
    path("photo/delete/<int:pk>/", PhotoDeleteView.as_view(), name="photo_delete")
]