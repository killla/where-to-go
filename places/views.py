from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse

from .models import Place, Image


def serialize_point(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": reverse(place_by_id, args=[place.pk])
        }
    }


def main_page(request):
    template = loader.get_template('index.html')
    places = Place.objects.all()

    points = {
        "type": "FeatureCollection",
        "features": [
            serialize_point(place) for place in places
        ]
    }

    context = {"points": points}
    rendered_page = template.render(context, request)

    return HttpResponse(rendered_page)


def place_by_id(request, pk):
    place = get_object_or_404(Place, pk=pk)
    point = {
        'title': place.title,
        'imgs': [image.photo.url for image in place.imgs.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
    }
    return JsonResponse(point, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
