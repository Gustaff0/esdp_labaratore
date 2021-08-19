from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

# Create your models here.

class Announcement(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(null=True, blank=True, validators=[MinLengthValidator(8)])

    class Meta:
        db_table = 'Announcements'
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявлении'


class Photo(models.Model):
    photo = models.ImageField(blank=False, null=False, upload_to='announcement_pics')
    announcement = models.ForeignKey('api_v1.Announcement', blank=False, null=False, related_name='photo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
