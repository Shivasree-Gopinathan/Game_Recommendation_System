from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from django.contrib.auth.decorators import login_required


@login_required
def make_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            Payment.objects.create(
                user=request.user,
                game_name=form.cleaned_data['game_name'],
                amount=form.cleaned_data['amount'],
            )
            # Redirect to a new URL:
            return redirect('success_url')  # Change 'success_url' to your success page's URL
    else:
        form = PaymentForm(initial={'game_name': request.GET.get('game_name', ''), 'amount': request.GET.get('amount', ' ')})

    return render(request, 'payment/payment.html', {'form': form})

#
# def payment_page(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             # user = form.save()  # Save the user to the database
#             #
#             # UserProfile.objects.create(user=user)
#             # login(request, user)  # Log in the user after successful signup
#             return redirect('payment_page')  # Redirect to signup success page
#     else:
#         form = PaymentForm()
#     return render(request, 'payment/payment.html', {'form': form})
#
#
# def process_payment(request):
#     if request.method == 'POST':
#         return render(request, 'payment/payment.html')
#     return redirect('payment_page')
