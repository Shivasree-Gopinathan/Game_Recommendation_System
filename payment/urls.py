# myapp/urls.py
import payment
from django.urls import path
from .views import payment, process_payment

urlpatterns = [
    path('', payment, name='payment'),
    path('process_payment/', process_payment, name='process_payment'),
    # Add other URL patterns as needed
]
