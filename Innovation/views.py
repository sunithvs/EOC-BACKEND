from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import viewsets, generics
from Innovation.models import Innovation

from Innovation.serializers import InnovationSerializer

class InnovationApiViewSet(viewsets.ModelViewSet, generics.GenericAPIView):
    queryset = Innovation.objects.all()
    serializer_class = InnovationSerializer
    http_method_names = ["get"]
 