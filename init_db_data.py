import pymongo
from datetime import datetime
from currency_api.enums import CurrencyDelimitor, CurrencyIdentificator, CurrencyIdentificatorPosition
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["currency"]
mycol = mydb["currency_api_currencyformat"]

x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

API_ENDPOINT = 'http://localhost:8000/api/currency-format/'

data = {
    "country_code": "USA",
    "currency_code": "USD",
    "currency_symbol": "$",
    "thousand_delimiter": str(CurrencyDelimitor.COMMA),
    "cents_delimiter": str(CurrencyDelimitor.DOT),
    "currency_identificator": str(CurrencyIdentificator.SYMBOL),
    "currency_identificator_position": str(CurrencyIdentificatorPosition.BEFORE),
    "is_show_cents": True
}
r = requests.post(url = API_ENDPOINT, data = data)
print(r)
data = {
    "country_code" : "ARG",
	"currency_code" : "USD",
	"currency_symbol" : "$",
	"thousand_delimiter" : str(CurrencyDelimitor.COMMA),
	"cents_delimiter" : str(CurrencyDelimitor.DOT),
	"currency_identificator" : str(CurrencyIdentificator.CODE),
	"currency_identificator_position" : str(CurrencyIdentificatorPosition.BEFORE),
	"is_show_cents" : False
}
r = requests.post(url = API_ENDPOINT, data = data)
print(r)
data = {
    "country_code" : "ESP",
	"currency_code" : "EUR",
	"currency_symbol" : "Є",
	"thousand_delimiter" : str(CurrencyDelimitor.COMMA),
	"cents_delimiter" : str(CurrencyDelimitor.DOT),
	"currency_identificator" : str(CurrencyIdentificator.CODE),
	"currency_identificator_position" : str(CurrencyIdentificatorPosition.AFTER),
	"is_show_cents" : False
}
r = requests.post(url = API_ENDPOINT, data = data)
print(r)
data = {
    "country_code" : "GER",
	"currency_code" : "EUR",
	"currency_symbol" : "Є",
	"thousand_delimiter" : str(CurrencyDelimitor.DOT),
	"cents_delimiter" : str(CurrencyDelimitor.COMMA),
	"currency_identificator" : str(CurrencyIdentificator.CODE),
	"currency_identificator_position" : str(CurrencyIdentificatorPosition.BEFORE),
	"is_show_cents" : False
}
r = requests.post(url = API_ENDPOINT, data = data)
print(r)
data = {
    "country_code" : "CHL",
	"currency_code" : "USD",
	"currency_symbol" : "$",
	"thousand_delimiter" : str(CurrencyDelimitor.DOT),
	"cents_delimiter" : str(CurrencyDelimitor.COMMA),
	"currency_identificator" : str(CurrencyIdentificator.CODE),
	"currency_identificator_position" : str(CurrencyIdentificatorPosition.BEFORE),
	"is_show_cents" : True
}
r = requests.post(url = API_ENDPOINT, data = data)
print(r)