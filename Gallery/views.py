from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Gallery.models import Programs

from Gallery.serializers import GallerySerializer, MentorSerializer, Mentor
import django_filters


@csrf_exempt
def galleryApi(request):
    if request.method == 'GET':
        posts = Programs.objects.all()
        post_serializer = GallerySerializer(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)


class ProgramApiViewSet(viewsets.ModelViewSet, generics.GenericAPIView):
    queryset = Programs.objects.all().filter().order_by('-ProgramDate')
    serializer_class = GallerySerializer
    http_method_names = ["get"]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['type']


class MentorApiViewSet(viewsets.ModelViewSet, generics.GenericAPIView):
    queryset = Mentor.objects.all().all()
    serializer_class = GallerySerializer
    http_method_names = ["get"]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['type']
