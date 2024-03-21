from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from django.contrib.auth.decorators import login_required


@login_required
def make_payment(request):
    success_message = ''
    game_name = request.GET.get('game_name', '')
    amount = request.GET.get('amount', '')
    initial_data = {
        'game_name': request.GET.get('game_name', ''),  # Adjusted to 'title'
        'amount': request.GET.get('amount', '')  # Adjusted to 'price'
    }
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['credit_card_number']
            card_last_four = card_number[-4:]
            payment = Payment(
                user=request.user,
                game_name=initial_data['game_name'],
                amount=initial_data['amount'],
                card_last_four=card_last_four,
            )
            payment.save()
            success_message = "Payment successful!"
        else:
            form.fields['game_name'].initial = game_name
            form.fields['amount'].initial = amount
    else:
        initial_data = {'game_name': game_name, 'amount': amount}
        form = PaymentForm(initial=initial_data)

    return render(request, 'payment/payment.html', {'form': form, 'success_message': success_message,
                                                    'game_name': game_name, 'amount': amount})


@login_required
def payment_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-payment_date')
    return render(request, 'payment/history.html', {'payments': payments})

