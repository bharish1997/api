from django.shortcuts import render
import requests as r
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


# Create your views here.
@api_view(['GET'])
def ping_view(request):
    if request.method == 'GET':
        return Response({"status": "OK"}, status=200)


@api_view(['GET'])
def first(request):
    if str(request.GET.get('dt')) == str(datetime.now().replace(second=0, microsecond=0)):
        re = r.get(request.GET.get('url'))
        return Response(status=re.status_code)
    else:
        return Response(status=401)