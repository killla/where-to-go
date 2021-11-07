from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
            "detailsUrl": "some.json"
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
