from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = HTMLField('Длинное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    number = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField()
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место', related_name='imgs')

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place}'
