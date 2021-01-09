from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def ping_view(request):
    if request.method == 'GET':
        return Response(status=200)
