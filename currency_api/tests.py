from django.test import TestCase
from .util import CurrencyAmount
from .enums import CurrencyIdentificator, CurrencyIdentificatorPosition, CurrencyDelimitor

class CurrencyAmountTestCase(TestCase):
    def setUp(self):
        None

    def test_currency_amount_01(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = True, 
            amount = 234.56
        )
        self.assertEqual(us_currency.display_in_format(), "$ 234.56")
    
    def test_currency_amount_02(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = True, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "$ 1,234.56")

    def test_currency_amount_03(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.AFTER,
            is_show_cents = True, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "1,234.56 $")

    def test_currency_amount_04(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.CODE, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = True, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "USD 1,234.56")
    
    def test_currency_amount_05(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.CODE, 
            currency_identificator_position = CurrencyIdentificatorPosition.AFTER,
            is_show_cents = True, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "1,234.56 USD")

    def test_currency_amount_06(self):
        us_currency = CurrencyAmount(
            currency_code = "EUR",
            currency_symbol = "Є" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.CODE, 
            currency_identificator_position = CurrencyIdentificatorPosition.AFTER,
            is_show_cents = False, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "1,234 EUR")

    def test_currency_amount_07(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.CODE, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = False, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "USD 1,234")

    def test_currency_amount_08(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = False, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "$ 1,234")

    def test_currency_amount_09(self):
        us_currency = CurrencyAmount(
            currency_code = "EUR",
            currency_symbol = "Є" , 
            thousand_delimiter = CurrencyDelimitor.COMMA, 
            cents_delimiter = CurrencyDelimitor.DOT, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.AFTER,
            is_show_cents = False, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "1,234 Є")

    def test_currency_amount_10(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.DOT, 
            cents_delimiter = CurrencyDelimitor.COMMA, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = True, 
            amount = 1234.56
        )
        self.assertEqual(us_currency.display_in_format(), "$ 1.234,56")

    def test_currency_amount_11(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.DOT, 
            cents_delimiter = CurrencyDelimitor.COMMA, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = True, 
            amount = 1234.00
        )
        self.assertEqual(us_currency.display_in_format(), "$ 1.234,00")
    
    def test_currency_amount_12(self):
        us_currency = CurrencyAmount(
            currency_code = "USD",
            currency_symbol = "$" , 
            thousand_delimiter = CurrencyDelimitor.DOT, 
            cents_delimiter = CurrencyDelimitor.COMMA, 
            currency_identificator = CurrencyIdentificator.SYMBOL, 
            currency_identificator_position = CurrencyIdentificatorPosition.BEFORE,
            is_show_cents = True, 
            amount = 234.56
        )
        self.assertEqual(us_currency.display_in_format(), "$ 234,56")

    

        

        
