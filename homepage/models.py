from django.db import models
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)  # Field for genre name
    image = models.ImageField(upload_to='genre_images/')  # Field for genre image

    def __str__(self):
        return self.name


# Create your models here.
