from django.urls import path, include
from rest_framework.routers import DefaultRouter

from currency_api import views

router = DefaultRouter()
router.register('currency-format', views.CurrencyFormatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]