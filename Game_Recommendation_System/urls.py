"""
URL configuration for Game_Recommendation_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from homepage.views import contact, nonuser
from django.contrib import admin
from django.urls import path, include

from homepage import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/',include('homepage.urls')),
    path('game/',include('game.urls')),
    path('games/', views.showgames, name='showgames'),
    path('contact/',contact, name='contact'),
    path('nonuser/',nonuser, name='nonuser'),
    path('', include('payment.urls')),
    path('', include('user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


