from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='phote',
                              null=False,
                              blank=False,
                              verbose_name='Картинка')
    signature = models.CharField(max_length=200,
                                 null=False,
                                 blank=False,
                                 verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        related_name='photos'
    )
    album = models.ForeignKey('webapp.Album',
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True,
                              related_name='photos')
    private = models.BooleanField(default=False,
                                  verbose_name='Статус')
    token = models.UUIDField(null=True,
                             blank=True,
                             verbose_name='Токен')


class Album(models.Model):
    name = models.CharField(max_length=200,
                            null=False,
                            blank=False,
                            verbose_name='Название')
    description = models.TextField(max_length=2000,
                                   null=True,
                                   blank=True,
                                   verbose_name='Описание')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=False,
        related_name='albums'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False, verbose_name='Статус')


class PhotoFavorites(models.Model):
    author = models.ForeignKey(get_user_model(), related_name="photo_favorite", on_delete=models.CASCADE)
    photo = models.ForeignKey("webapp.Photo", related_name="favorite", on_delete=models.CASCADE)

    class Meta:
        db_table = "photo_favorite"
        verbose_name = "Избранное фото"
        verbose_name_plural = "Избранные фото"

class AlbumFavorites(models.Model):
    author = models.ForeignKey(get_user_model(), related_name="album_favorite", on_delete=models.CASCADE)
    album = models.ForeignKey("webapp.Album", related_name="favorites", on_delete=models.CASCADE)

    class Meta:
        db_table = "album_favorite"
        verbose_name = "Избранный альбом"
        verbose_name_plural = "Избранные альбомы"