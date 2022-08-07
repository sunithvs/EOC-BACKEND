from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Carousel.models import carousel

from Carousel.serializers import CarouselSerializer


@csrf_exempt
def CarouselApi(request):
    if request.method == 'GET':
        carouselitem = carousel.objects.all()
        item_serializer = CarouselSerializer(carouselitem,many=True)
        return JsonResponse(item_serializer.data,safe=False)