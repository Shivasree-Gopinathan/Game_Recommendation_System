from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
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

    def __str__(self):
        return f'{self.title}'


