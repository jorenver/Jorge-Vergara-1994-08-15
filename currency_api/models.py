from djongo import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from .enums import CurrencyIdentificator, CurrencyDelimitor, CurrencyIdentificatorPosition


class UserCurrencyManager(BaseUserManager):
    ''' Manager para perfiles de Usuario '''

    def create_user(self, email, name, password=None):
        ''' Crear Nuevo User Profile '''
        if not email: 
            raise ValueError('Usuario debe tener un Email')

        email = self.normalize_email(email)
        
        user = self.model(email = email, name= name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserCurrency(AbstractBaseUser, PermissionsMixin):
    ''' Modelo Base de datos para usuarios en el sistema '''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserCurrencyManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        ''' Obtener Nombre Completo del usuario'''
        return self.name
    
    def get_short_name(self):
        ''' Obtener Nombre Corto del usuario '''
        return self.name
    
    def __str__(self):
        ''' Cadena para representar al usuario '''
        return self.email

class CurrencyFormat(models.Model):
    ''' Currency Formats model '''
    created_on = models.DateTimeField(auto_now_add=True)
    country_code = models.CharField( max_length=50)
    currency_code = models.CharField(max_length=50)
    currency_symbol = models.CharField(max_length=1)
    thousand_delimiter = models.CharField(
        max_length=1, 
        choices = CurrencyDelimitor.choices(),
        default = CurrencyDelimitor.COMMA
    )
    cents_delimiter = models.CharField(
        max_length=1,
        choices = CurrencyDelimitor.choices(),
        default = CurrencyDelimitor.DOT
    )
    currency_identificator = models.CharField(
        max_length=10,
        choices = CurrencyIdentificator.choices(),
        default=CurrencyIdentificator.SYMBOL
    )
    currency_identificator_position = models.CharField(
        max_length=10,
        choices = CurrencyIdentificatorPosition.choices(),
        default=CurrencyIdentificatorPosition.BEFORE
    )
    is_show_cents = models.BooleanField()

    class Meta:
        unique_together = ('country_code', 'currency_code',)
    def __str__(self):
        return "{0} {1}".format(self.country_code, self.currency_code)