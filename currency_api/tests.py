from django.test import TestCase
from .util import CurrencyAmount

class CurrencyAmountTestCase(TestCase):
    def setUp(self):
        None

    def test_us_currency(self):
        us_currency = CurrencyAmount(
            currency_symbol ="USD" , 
            thousand_delimiter = ",", 
            cents_delimiter = '.', 
            currency_identificator = 'SYMBOL', 
            currency_identificator_position = 'BEFORE',
            is_show_cents = True, 
            amount = 1723.55
        )
        self.assertEqual(us_currency.display_in_format(), '$ 1,723.55')
