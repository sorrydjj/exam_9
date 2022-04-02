from django.urls import path

from webapp.views import Views

app_name = "webapp"

urlpatterns = [
    path("gallery", Views.as_view())
]