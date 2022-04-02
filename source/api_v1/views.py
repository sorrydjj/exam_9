import json

from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly, IsAdminUser, \
    DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from webapp.models import PhotoFavorites, AlbumFavorites

from api_v1.serializers import PhotoFavoriteSerializer


class PhotoFavoriteCreateSet(ModelViewSet):
    queryset = PhotoFavorites.objects.all()
    serializer_class = PhotoFavoriteSerializer

    def destroy(self, request, *args, **kwargs):
        body = json.loads(request.body)
        print(body)
        if PhotoFavorites.objects.filter(photo=body["photo"]):
            photo = PhotoFavorites.objects.filter(photo=body["photo"])
            photo.delete()
            return super().destroy(request, *args, **kwargs)
