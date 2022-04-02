import http
import json

from rest_framework import serializers
from rest_framework.response import Response

from webapp.models import PhotoFavorites, AlbumFavorites


class PhotoFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoFavorites
        fields = ("author", "photo",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        if PhotoFavorites.objects.filter(photo=validated_data["photo"]):
            return
        else:
            photo_fav = PhotoFavorites()
            photo_fav.author = validated_data["author"]
            photo_fav.photo = validated_data["photo"]
            photo_fav.save()
            return photo_fav