from django.urls import path

from payment import views

urlpatterns = [
    path('payments', views.make_payment, name='payments'),
    path('payment/history', views.payment_history, name='payment_history'),
]