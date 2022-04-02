from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from webapp.models import Photo, Album, PhotoFavorites, AlbumFavorites

from webapp.forms import PhotoFavoriteForm


class PhotoAddFavoriteView(LoginRequiredMixin, CreateView):
    model = PhotoFavorites
    template_name = "phote/create.html"
    form_class = PhotoFavoriteForm

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        if PhotoFavorites.objects.filter(photo=photo, author=self.request.user):
            pass
        else:
            PhotoFavorites.objects.create(photo=photo, author=self.request.user)
        return JsonResponse({"status": "add"})


class PhotoDeleteFavoriteView(LoginRequiredMixin, CreateView):
    model = PhotoFavorites
    template_name = "phote/create.html"
    form_class = PhotoFavorites

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        favorite = PhotoFavorites.objects.filter(photo=photo, author=self.request.user)
        if favorite:
            favorite.delete()
        return JsonResponse({"status": "delete"})