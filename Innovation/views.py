from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Innovation.models import Innovation

from Innovation.serializers import InnovationSerializer


@csrf_exempt
def InnovationApi(request):
    if request.method == 'GET':
        posts = Innovation.objects.all()
        post_serializer = InnovationSerializer(posts,many=True)
        return JsonResponse(post_serializer.data,safe=False)