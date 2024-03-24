from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_last_four = models.CharField(max_length=4)
    payment_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user} - {self.game_name} - {self.amount}"
