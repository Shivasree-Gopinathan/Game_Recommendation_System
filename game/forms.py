from django import forms
from .models import GameReview


class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ['rating', 'review']
        widgets = {
            'rating': forms.NumberInput(attrs={'step': '0.1'}),  # Allow decimal steps
            'review': forms.Textarea(attrs={'rows': 4}),
        }