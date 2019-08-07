from django import forms

from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'title',
            'description',
            'stage'
        ]

    def save(self,board):
        card = super(CardForm,self).save(commit=False)
        card.board = board
        card.save()
        return card
