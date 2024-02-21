from django.shortcuts import render
from django.contrib.auth.models import User


def payment(request):
    users = User.objects.all()  # Fetch all users (you can modify this query as needed)
    return render(request, 'payment.html', {'users': users})


def process_payment(request):
    # Your process_payment view logic here
    return render(request, 'process_payment.html')
from django.shortcuts import render

# Create your views here.
