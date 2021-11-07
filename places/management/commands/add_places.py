from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image


def get_filename(url):
    image_path = urlparse(url).path
    filename = image_path.split('/')[-1]
    return filename


class Command(BaseCommand):
    help = 'Loads places description and photos to database'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        data = response.json()
        title = data['title']
        description_short = data['description_short']
        description_long = data['description_long']
        lng = data['coordinates']['lng']
        lat = data['coordinates']['lat']

        place, created = Place.objects.update_or_create(
            title=title,
            description_short=description_short,
            description_long=description_long,
            lng=lng,
            lat=lat,
        )

        image_urls = data['imgs']
        if not created:
            images = place.images.all()
            images.delete()

        for number, url in enumerate(image_urls):
            image = Image.objects.create(place=place, number=number)
            image_response = requests.get(url)
            image_response.raise_for_status()
            content = ContentFile(image_response.content)
            filename = get_filename(url)
            image.photo.save(filename, content, save=True)
