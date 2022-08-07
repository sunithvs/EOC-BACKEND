from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Gallery.models import Programs

from Gallery.serializers import GallerySerializer


@csrf_exempt
def galleryApi(request):
    if request.method == 'GET':
        posts = Programs.objects.all()
        post_serializer = GallerySerializer(posts,many=True)
        return JsonResponse(post_serializer.data,safe=False)