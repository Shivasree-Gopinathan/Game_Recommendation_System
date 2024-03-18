from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('<int:game_id>/', views.game_details, name='game_details'),
    path('<int:game_id>/add_review/', views.add_review, name='add_review'),
]