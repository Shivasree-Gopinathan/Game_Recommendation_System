from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=20)
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='../images/', blank=False)
    avg_rating = models.FloatField()

    def __str__(self):
        return f'{self.title}'


