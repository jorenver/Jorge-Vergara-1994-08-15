class CurrencyAmount:

    def __init__(self,currency_symbol, thousand_delimiter, cents_delimiter, 
    currency_identificator, currency_identificator_position,is_show_cents, amount ):
        self.currency_symbol = currency_symbol
        self.thousand_delimiter = thousand_delimiter
        self.cents_delimiter = cents_delimiter
        self.currency_identificator = currency_identificator
        self.currency_identificator_position = currency_identificator_position
        self.is_show_cents = is_show_cents
        self.amount = amount

    def display_in_format(self):
        return ""

