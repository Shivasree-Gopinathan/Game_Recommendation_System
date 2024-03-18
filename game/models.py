from django.contrib.auth.models import User
from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    platforms = models.ManyToManyField(Platform)
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=False)
    avg_rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f'{self.title}'


class GameReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    rating = models.FloatField()
    review = models.TextField()

    def _str_(self):
        return f"Review by {self.user.username} for {self.game.title}"