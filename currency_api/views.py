from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.decorators import action
from currency_api import serializer, models
from .util import CurrencyAmount

class CurrencyFormatViewSet(viewsets.ModelViewSet):
    ''' CRUD Currency Format '''
    serializer_class = serializer.CurrencyFormatSerializer
    queryset = models.CurrencyFormat.objects.all()

    def create(self, request):
        ''' CREAD NEW CURRENCY FORMAT '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'message': 'Currency format created', 
                'pk': serializer.instance.pk
            })
        else:
           return Response(
               serializer.errors,
               status = status.HTTP_400_BAD_REQUEST
           )

class CurrencyAmountView(APIView):
    serializer_class = serializer.CurrencyAmountSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            country_code = serializer.validated_data.get('country_code')
            currency_code = serializer.validated_data.get('currency_code')
            amount = serializer.validated_data.get('amount')
            
            cunrrency_format_list = models.CurrencyFormat.objects.filter(
                country_code=country_code, 
                currency_code=currency_code
                )
            
            if len(cunrrency_format_list) !=1:
                print ("invalid currency!")
                return Response({
                    "error": True,
                    "message": "invalid currency!"
                },status=status.HTTP_406_NOT_ACCEPTABLE)
            
            currency_amount = CurrencyAmount(
                currency_code = currency_code,
                currency_symbol = cunrrency_format_list[0].currency_symbol, 
                thousand_delimiter = cunrrency_format_list[0].thousand_delimiter, 
                cents_delimiter = cunrrency_format_list[0].cents_delimiter, 
                currency_identificator = cunrrency_format_list[0].currency_identificator, 
                currency_identificator_position = cunrrency_format_list[0].currency_identificator_position,
                is_show_cents = cunrrency_format_list[0].is_show_cents, 
                amount = amount
            )

            display_amount = currency_amount.display_in_format()
            print(display_amount)
            return Response({
                'country_code': country_code, 
                'currency_code': currency_code,
                'amount': amount,
                'displayed_amount': display_amount
            })
        else:
           return Response(
               serializer.errors,
               status = status.HTTP_400_BAD_REQUEST
           )

        