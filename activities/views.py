from django.shortcuts import render
from rest_framework import viewsets, generics

from activities.models import Activity
from activities.serializers import ActivitySerializer


class ActivityApiViewSet(viewsets.ModelViewSet, generics.GenericAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    http_method_names = ["get"]
