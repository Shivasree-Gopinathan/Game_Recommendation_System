from django.urls import path
from . import views

myapp = 'myapp'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('login/', views.login_view, name='login'),
    path('login/success/', views.login_success, name='login_success'),
]
