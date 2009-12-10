import re
from django import newforms as forms

class CurrencyField(forms.RegexField):
    currencyRe = re.compile(r'^[0-9]{1,5}(.[0-9][0-9])?$')
    def __init__(self, *args, **kwargs):
        super(CurrencyField, self).__init__(
            self.currencyRe, None, None, *args, **kwargs)

    def clean(self, value):
        value = super(CurrencyField, self).clean(value)
        return float(value)

class CurrencyInput (forms.TextInput):
    def render(self, name, value, attrs=None):c
        if value != '':
            try:
                value = u"%.2f" % value
            except TypeError:
                pass
        return super(CurrencyInput, self).render(name, value, attrs)

class MyForm (forms.Form):
    amount = CurrencyField(widget=CurrencyInput, initial=5)
