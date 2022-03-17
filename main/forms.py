from django import forms
from main.models import FlashCard


class FlashCardForm(forms.Form):
    category = forms.CharField()
    cue = forms.CharField()
    cue_expanded = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}), required=False)
    info = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
