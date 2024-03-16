from django.db import models
from django.contrib.auth.models import User
from homepage.models import Genre

# class User(models.Model):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     date_joined = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    favourite_genre = models.CharField(max_length=100, blank=True)
    # favourite_genre = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.user.username
