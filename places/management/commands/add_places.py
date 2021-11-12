from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
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
        payload = response.json()

        place, created = Place.objects.update_or_create(
            title=payload['title'],
            description_short=payload['description_short'],
            lng=payload['coordinates']['lng'],
            lat=payload['coordinates']['lat'],
            defaults={'description_long': payload['description_long']}
        )

        image_urls = payload['imgs']
        if not created:
            place.imgs.all().delete()

        for number, url in enumerate(image_urls):
            image = Image.objects.create(place=place, number=number)
            image_response = requests.get(url)
            image_response.raise_for_status()
            content = ContentFile(image_response.content)
            filename = get_filename(url)
            image.photo.save(filename, content, save=True)
