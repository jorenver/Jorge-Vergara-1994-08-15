from enum import Enum
from django.utils.translation import ugettext_lazy as _

class CurrencyIdentificator(Enum):
    CODE = "CODE"
    SYMBOL = "SYMBOL"

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return (
            (str(cls.CODE), _("CODE")),
            (str(cls.SYMBOL), _("SYMBOL")),
        )

class CurrencyIdentificatorPosition(Enum):
    BEFORE = "BEFORE"
    AFTER = "AFTER"

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return (
            (str(cls.BEFORE), _("BEFORE")),
            (str(cls.AFTER), _("AFTER")),
        )

class CurrencyDelimitor(Enum):
    DOT = "."
    COMMA = ","

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return (
            (str(cls.DOT), _(".")),
            (str(cls.COMMA), _(",")),
        )
