from django import forms
from django.core.validators import MinLengthValidator, RegexValidator
from django.forms.widgets import NumberInput
import datetime


class PaymentForm(forms.Form):
    game_name = forms.CharField(max_length=100)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    credit_card_number = forms.CharField(
        validators=[MinLengthValidator(16), RegexValidator(r'^\d{16}$', message="Must be a 16 digit number")])
    month = forms.CharField(
        validators=[RegexValidator(r'^(0[1-9]|1[0-2])$', message="Must be a valid month (01-12)")])
    year = forms.CharField(
        validators=[RegexValidator(r'^\d{4}$', message="Must be a valid year in YYYY format")])
    cvv = forms.CharField(
        validators=[MinLengthValidator(3), RegexValidator(r'^\d{3}$', message="Must be a 3 digit number")])

    # def clean_month_year(self):
    #     month_year = self.cleaned_data.get('month_year')
    #     if month_year and month_year < datetim e.date.today().replace(day=1):
    #         print(month_year)
    #         raise forms.ValidationError("The date must be in the future.")
    #     else:
    #         print(month_year)
    #         print(datetime.date.today())
    #     return month_year
