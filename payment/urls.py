from django.urls import path

from payment import views

urlpatterns = [
    path('payment_page', views.make_payment, name='payment_page'),
    # path('process_payment/', views.make_payment, name='process_payment'),
]