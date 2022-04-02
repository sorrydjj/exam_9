import uuid

from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from secrets import token_urlsafe

from webapp.models import Photo, Album
from webapp.forms import PhotoForm



class PhotoListView(ListView):
    template_name = 'phote/index.html'
    model = Photo

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs["photos"] = Photo.objects.filter(private=False).order_by("-created_at")
        return kwargs


class PhotoDetailView(DetailView):
    template_name = 'phote/detail.html'
    model = Photo
    context_object_name = "photo"


class PhotoCreateView(CreateView):
    template_name = "phote/create.html"
    model = Photo
    form_class = PhotoForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['album'] = Album.objects.filter(author=self.request.user)
        return kwargs

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.token = uuid.uuid4()
        photo.save()
        return redirect("webapp:index")


class PhotoUpdateView(UpdateView):
    template_name = "phote/update.html"
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return reverse("webapp:index")


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = "phote/delete.html"

    def post(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:index")