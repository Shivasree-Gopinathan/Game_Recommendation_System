from django.shortcuts import render, redirect

from django.shortcuts import render

from .forms import GameReviewForm
from .models import Game, GameReview
from django.shortcuts import get_object_or_404
from django.views import View


# Create your views here.

def game_details(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    game_review = GameReview.objects.filter(game=game)
    for review in game_review:
        review.stars = render_stars(review.rating)
    similar_genre_games = Game.objects.filter(genre=game.genre).exclude(id=game_id)[:]
    return render(request, 'game/game_details.html', {'game': game, 'game_review': game_review, 'similar_genre_games': similar_genre_games})


def render_stars(rating):
    filled_stars = '★' * int(rating)
    empty_stars = '☆' * (5 - int(rating))
    return filled_stars + empty_stars


def add_review(request, game_id):
    game = Game.objects.get(pk=game_id)
    if request.method == 'POST':
        form = GameReviewForm(request.POST)
        print(form)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.user = request.user
            review.save()
            return redirect('game_details', game_id=game_id)
    else:
        form = GameReviewForm()
    return render(request, 'game/add_review_old.html', {'form': form, 'game': game})

