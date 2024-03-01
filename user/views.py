from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_profile(request):
    text = "Hello from user_profile"
    response = HttpResponse(text, content_type="text/plain")
    return response
