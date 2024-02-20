from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    response = HttpResponse()
    heading = '<h1>' + 'Welcome to Games Home page' + '</h1>'
    about = '<p>' + 'This is a game recommendation website' + '</p>'
    bgcolor = '<body style= background-color:cyan>'
    response.write(heading)
    response.write(about)
    response.write(bgcolor)
    return response
    #return render(request, 'homepage.html')


# Create your views here.
