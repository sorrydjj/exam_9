from django import forms

from webapp.models import Photo, Album, PhotoFavorites, AlbumFavorites

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'signature', 'album', 'private',)
        labels = {
            "private": 'Сделать приватным'
        }

    def __init__(self, *args, **kwargs):
        albums = kwargs.pop('album')
        super().__init__(*args, **kwargs)
        self.fields['album'].queryset = albums


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'description', 'private')
        labels = {
            "private": 'Сделать приватным'
        }


class PhotoFavoriteForm(forms.ModelForm):
    class Meta:
        model = PhotoFavorites
        fields = ("author", "photo")

class AlbumFavoriteForm(forms.ModelForm):
    class Meta:
        model = AlbumFavorites
        fields = ("author", "album")