from django import forms


class LinkMatch(forms.Form):
    link = forms.CharField(max_length=10000, label='Участники матча', widget=forms.Textarea(attrs={'class': 'form-control'}))
