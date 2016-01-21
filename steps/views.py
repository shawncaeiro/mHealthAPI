from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from models import Health

# Create your views here.

class HealthView(APIView):
    """
    View for processing Home Timeline request
    """

    def get(self, request):
        return Response({"hi": 3}, status=status.HTTP_200_OK)