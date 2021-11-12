from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


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
            "detailsUrl": reverse(get_place, args=[place.pk])
        }
    }


def get_map(request):
    places = Place.objects.all()
    points = {
        "type": "FeatureCollection",
        "features": [
            serialize_point(place) for place in places
        ]
    }
    return render(request, 'index.html', context={"points": points})


def get_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    point = {
        'title': place.title,
        'imgs': [image.photo.url for image in place.imgs.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
    }
    return JsonResponse(point, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
