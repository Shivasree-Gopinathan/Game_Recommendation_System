from django.urls import path
from . import views
from homepage.views import home


my_app = 'user'
urlpatterns = [
    path('', views.signup, name='signup'),  # URL for the signup page
    path('signup/success/', views.login, name='signup_success'),
    path('login/', views.login_view, name='login'),
    path('home/', home, name='home'),
]
# URL for the signup success page
    # Add other URLs for your app as needed

