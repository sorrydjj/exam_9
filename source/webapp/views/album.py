from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from secrets import token_urlsafe

from webapp.models import Album, Photo
from webapp.forms import AlbumForm

class AlbumDetailView(LoginRequiredMixin, DetailView):
    template_name = 'album/detail.html'
    model = Album
    context_object_name = "album"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = Photo.objects.filter(album=self.kwargs.get("pk"))
        context["photo_list"] = photo
        return context

class AlbumCreateView(LoginRequiredMixin, CreateView):
    template_name = "album/create.html"
    model = Album
    form_class = AlbumForm

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author = self.request.user
        album.save()
        return redirect("webapp:index")


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "album/update.html"
    model = Album
    form_class = AlbumForm
    permission_required = "webapp.change_album"

    def get_success_url(self):
        return reverse("webapp:album_detail", kwargs={"pk": self.object.pk})

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()

class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "album/delete.html"
    model = Album
    permission_required = "webapp.delete_album"

    def post(self, request, *args, **kwargs):
        photos = Photo.objects.filter(album=self.kwargs.get("pk"))
        photos.delete()
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:index")

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()