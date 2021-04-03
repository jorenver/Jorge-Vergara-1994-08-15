from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from currency_api import serializer, models

class CurrencyFormatViewSet(viewsets.ModelViewSet):
    ''' CRUD Currency Format '''
    serializer_class = serializer.CurrencyFormatSerializer
    queryset = models.CurrencyFormat.objects.all()

    def create(self, request):
        ''' CREAD NEW CURRENCY FORMAT '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Currency format created'})
        else:
           return Response(
               serializer.errors,
               status = status.HTTP_400_BAD_REQUEST
           ) 
