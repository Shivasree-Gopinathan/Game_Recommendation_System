from django.shortcuts import render
from game.models import Game

def home(request):
    games = Game.objects.all()
    action_games = Game.objects.filter(genre__icontains='Action')
    adventure_games = Game.objects.filter(genre__icontains='Adventure')
    simulation_games = Game.objects.filter(genre__icontains='Simulation')
    puzzle_games = Game.objects.filter(genre__icontains='Puzzle')
    roleplay_games = Game.objects.filter(genre__icontains='Role-play')

    context = {
        'action_games': action_games,
        'adventure_games': adventure_games,
        'simulation_games': simulation_games,
        'puzzle_games': puzzle_games,
        'roleplay_games': roleplay_games,
        'games': games,
    }
    return render(request, 'homepage/homepage.html', context)

def genre(request):
    unique_genres = Game.objects.values_list('genre', flat=True).distinct()
    context = {
        'unique_genres': unique_genres,
    }
    return render(request, 'homepage/genre.html', context)

def game_search(request):
    query = request.GET.get('q')
    if query:
        games = Game.objects.filter(title__icontains=query)
    else:
        games = Game.objects.all()
    return render(request, 'game_search.html', {'games': games})

