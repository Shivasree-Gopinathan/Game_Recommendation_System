from django.shortcuts import render

from homepage.forms import ContactForm
from homepage.models import Genre
from game.models import Game, Platform
from datetime import datetime
from functools import reduce
from django.db.models import Q

def home(request):
    games = Game.objects.all()
    # print(games[0].image.url)
    genre = Genre.objects.all()
    visit_count = request.session.get('visit_count',0)
    visit_count += 1
    request.session['visit_count'] = visit_count
    return render(request, 'homepage/homepage.html', {'games': games, 'genre': genre,'visit_count':visit_count})


def genre(request):
    unique_genres = Game.objects.values_list('genre', flat=True).distinct()
    context = {
       'unique_genres': unique_genres,
    }
    return render(request, 'homepage/homepage.html', context)

# def game_search(request):
#     query = request.GET.get('q')
#     if query:
#         games = Game.objects.filter(title__icontains=query)
#     else:
#         games = Game.objects.all()
#     return render(request, 'game_search.html', {'games': games})
def showgames(request):
    games = Game.objects.all().distinct()
    query = request.GET.get('q')
    genre = request.GET.get('genre')
    platform = request.GET.get('platform')

    unique_genres = set()
    for game in games:
        unique_genres.update(game.genre.split(","))
    unique_genres = sorted(list(unique_genres))

    ld = datetime(2021, 1, 1)
    lessdategames = Game.objects.filter(release_date__gte=ld)
    pc_platform = Platform.objects.get(name='Windows PC')
    pcgames = Game.objects.filter(platforms=pc_platform)
    main_content = 1

    if query or genre:
        main_content = 0
        games = games.filter(title__icontains=query).distinct()
    if genre:
        # Split the input genre string and filter games based on any matching genre
        genres_list = [g.strip() for g in genre.split(",")]
        genre_filter = reduce(lambda x, y: x | y, [Q(genre__icontains=g) for g in genres_list])
        games = games.filter(genre_filter)
    if platform:
        games = games.filter(platform__icontains=platform)

    return render(request, 'homepage/showgames.html', {'games': games, 'unique_genres': unique_genres, 'less_dategames': lessdategames, 'pcgames': pcgames, 'main_content': main_content})

def nonuser(request):
    games = Game.objects.all()
    genre = Genre.objects.all()
    return render(request, 'homepage/non_user.html', {'games': games, 'genre': genre})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            form.save()
            # Redirect to a success page or back to the contact page
            # return render(request,  'homepage/homepage.html')
            # {'success_message': 'Thank you for contacting us, we will get back to you soon!'}
    else:
        form = ContactForm()
    return render(request, 'homepage/contact.html', {'form': form})

