from django.urls import path
from . import views
from homepage.views import home
from django.contrib.auth import views as auth_views

my_app = 'user'
urlpatterns = [
    path('', views.signup, name='signup'),  # URL for the signup page
    path('signup/success/', views.login, name='signup_success'),
    path('login/', views.login_view, name='login'),
    path('home/', home, name='home'),
    path('profile/', views.view_profile, name='view_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='user/password_reset_form.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'
    ), name='password_reset_complete'),
]

