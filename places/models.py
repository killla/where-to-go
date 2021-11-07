from django.db import models


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Короткое описание')
    description_long = models.TextField('Длинное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    number = models.SmallIntegerField()
    photo = models.ImageField()
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место', related_name='imgs')
    def __str__(self):
        return f'{self.number} {self.place}'
