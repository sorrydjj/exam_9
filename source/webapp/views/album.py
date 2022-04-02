from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from secrets import token_urlsafe

from webapp.models import Album, Photo
from webapp.forms import AlbumForm

class AlbumDetailView(DetailView):
    template_name = 'album/detail.html'
    model = Album
    context_object_name = "album"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = Photo.objects.filter(album=self.kwargs.get("pk"))
        context["photo_list"] = photo
        print(context["photo_list"])
        for i in context["photo_list"]:
            print(i.pk)
        return context

class AlbumCreateView(CreateView):
    template_name = "album/create.html"
    model = Album
    form_class = AlbumForm

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author = self.request.user
        album.save()
        return redirect("webapp:index")


class AlbumUpdateView(UpdateView):
    template_name = "album/update.html"
    model = Album
    form_class = AlbumForm

    def get_success_url(self):
        return reverse("webapp:album_detail", kwargs={"pk": self.object.pk})


class AlbumDeleteView(DeleteView):
    template_name = "album/delete.html"
    model = Album

    def post(self, request, *args, **kwargs):
        photos = Photo.objects.filter(album=self.kwargs.get("pk"))
        photos.delete()
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:index")