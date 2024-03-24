from django import forms
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
import datetime


class PaymentForm(forms.Form):
    game_name = forms.CharField(max_length=100, disabled=True, required=False)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, disabled=True, required=False)
    credit_card_number = forms.CharField(
        validators=[MinLengthValidator(16), RegexValidator(r'^\d{16}$', message="Must be a 16 digit number")])
    expiry_date = forms.CharField(
        validators=[RegexValidator(r'^(0[1-9]|1[0-2])\/\d{2}$', message="Must be in MM/YY format")])
    cvv = forms.CharField(
        validators=[MinLengthValidator(3), RegexValidator(r'^\d{3}$', message="Must be a 3 digit number")])

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data.get('expiry_date')
        try:
            month, year = expiry_date.split('/')
            month, year = int(month), int(year) + 2000  # Assuming expiry_date is in MM/YY format
            # Check if the expiry date is in the past
            if datetime.date(year, month, 1) < datetime.date.today().replace(day=1):
                raise ValidationError("The expiry date must be in the future.")
        except ValueError:
            raise ValidationError("Invalid expiry date format.")
        return expiry_date
