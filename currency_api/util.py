from .enums import CurrencyIdentificator, CurrencyIdentificatorPosition

class CurrencyAmount:

    def __init__(self,currency_code, currency_symbol, thousand_delimiter, cents_delimiter, 
    currency_identificator, currency_identificator_position,is_show_cents, amount ):
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        self.thousand_delimiter = thousand_delimiter
        self.cents_delimiter = cents_delimiter
        self.currency_identificator = currency_identificator
        self.currency_identificator_position = currency_identificator_position
        self.is_show_cents = is_show_cents
        self.amount = amount

    def display_in_format(self):
        amount_str = ""
        amount_bills = str(int(self.amount))
        amount_cents = str(int((self.amount*100)%100)).ljust(2, '0')
        chunk_len = 3
        amount_bills_chunks = []
        cnt = 0
        chunk = ""
        chunk_added = False
        for i in range(len(amount_bills)-1,-1,-1):
            chunk_added = False
            chunk = amount_bills[i] + chunk
            cnt = cnt + 1
            if cnt == chunk_len:
                chunk_added = True
                cnt = 0
                amount_bills_chunks.insert(0,chunk)
                chunk = ""
        
        if not chunk_added:
            amount_bills_chunks.insert(0,chunk)
        
        amount_bills_str = str(self.thousand_delimiter).join(amount_bills_chunks)
        
        if self.is_show_cents:
            amount_str = amount_bills_str + str(self.cents_delimiter) + amount_cents
        else:
            amount_str = amount_bills_str
        
        identificator = ""
        if str(self.currency_identificator) == str(CurrencyIdentificator.SYMBOL):
            identificator = self.currency_symbol
        else:
            identificator = self.currency_code


        if str(self.currency_identificator_position) == str(CurrencyIdentificatorPosition.BEFORE):
            amount_str = identificator +" "+ amount_str
        else:
            amount_str = amount_str +" "+identificator
        
        return amount_str

