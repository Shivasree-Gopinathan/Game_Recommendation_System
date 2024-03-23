from django.db import models
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)  # Field for genre name
    image = models.ImageField(upload_to='genre_images/')  # Field for genre image

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
