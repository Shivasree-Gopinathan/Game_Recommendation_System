from django.shortcuts import render
from .models import Game
from django.shortcuts import get_object_or_404
from django.views import View


# Create your views here.

def game_details(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/game_details.html', {'game': game})
