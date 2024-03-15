from django.shortcuts import render
from game.models import Game
from homepage.models import Genre
from functools import reduce
from django.db.models import Q

def home(request):
    games = Game.objects.all()
    genre = Genre.objects.all()
    return render(request, 'homepage/homepage.html', {'games': games, 'genre': genre})
    # action_games = Game.objects.filter(genre__icontains='Action')
    # adventure_games = Game.objects.filter(genre__icontains='Adventure')
    # simulation_games = Game.objects.filter(genre__icontains='Simulation')
    # puzzle_games = Game.objects.filter(genre__icontains='Puzzle')
    # roleplay_games = Game.objects.filter(genre__icontains='Role-play')
    #
    # context = {
    #     'action_games': action_games,
    #     'adventure_games': adventure_games,
    #     'simulation_games': simulation_games,
    #     'puzzle_games': puzzle_games,
    #     'roleplay_games': roleplay_games,
    #     'games': games,
    # }
def genre(request):
    unique_genres = Game.objects.values_list('genre', flat=True).distinct()
    context = {
        'unique_genres': unique_genres,
    }
    return render(request, 'homepage/homepage.html', context)

def game_search(request):
    query = request.GET.get('q')
    if query:
        games = Game.objects.filter(title__icontains=query)
    else:
        games = Game.objects.all()
    return render(request, 'game_search.html', {'games': games})

# def showgames(request):
#     games = Game.objects.all()
#     query = request.GET.get('q')
#     genre = request.GET.get('genre')
#     platform = request.GET.get('platform')
#
#     unique_genres = set()
#     for game in games:
#         unique_genres.update(game.genre.split(","))
#     unique_genres = sorted(list(unique_genres))
#
#     if query:
#         games = games.filter(title__icontains=query)
#     if genre:
#         games = games.filter(genre=genre)
#     if platform:
#         games = games.filter(platform__icontains=platform)
#
#     individual_genres = [g.strip() for genre in unique_genres for g in genre.split(",")]
#
#     return render(request, '../templates/homepage/showgames.html', {'games': games, 'unique_genres': individual_genres})


def showgames(request):
    games = Game.objects.all()
    query = request.GET.get('q')
    genre = request.GET.get('genre')
    platform = request.GET.get('platform')

    unique_genres = set()
    for game in games:
        unique_genres.update(game.genre.split(","))
    unique_genres = sorted(list(unique_genres))

    if query:
        games = games.filter(title__icontains=query)
    if genre:
        # Split the input genre string and filter games based on any matching genre
        genres_list = [g.strip() for g in genre.split(",")]
        genre_filter = reduce(lambda x, y: x | y, [Q(genre__icontains=g) for g in genres_list])
        games = games.filter(genre_filter)
    if platform:
        games = games.filter(platform__icontains=platform)

    return render(request, 'homepage/showgames.html', {'games': games, 'unique_genres': unique_genres})