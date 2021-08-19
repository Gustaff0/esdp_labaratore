from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Number(models.Model):
    number = models.IntegerField(blank=False, null=False, verbose_name='Номер', validators=[MinLengthValidator(8)])
    user = models.OneToOneField(get_user_model(), blank=False, null=False, related_name='number', verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Numbers'
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
