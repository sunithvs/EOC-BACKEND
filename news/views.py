from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from news.models import events
from news.serializers import eventSerializer


# Create your views here.
@csrf_exempt
def newsApi(request,id =0):
    if request.method=='GET':
        event = events.objects.all()        
        event_serializer = eventSerializer(event,many=True)
        return JsonResponse(event_serializer.data,safe=False)
    