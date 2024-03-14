from django.shortcuts import render
# from game.models import Game
from homepage.models import Genre

def home(request):
    # games = Game.objects.all()
    genre = Genre.objects.all()
    return render(request, 'homepage/homepage.html', { 'genre': genre})
# 'games': games,

def genre(request):
    #unique_genres = Game.objects.values_list('genre', flat=True).distinct()
    context = {
       # 'unique_genres': unique_genres,
    }
    return render(request, 'homepage/homepage.html', context)

# def game_search(request):
#     query = request.GET.get('q')
    # if query:
    #     games = Game.objects.filter(title__icontains=query)
    # else:
    #     games = Game.objects.all()
    # return render(request, 'game_search.html', {'games': games})

