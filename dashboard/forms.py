from django import forms
from players.models import Player, Team

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["nickname", "first_name", "last_name", "country", "team", "avatar", "flag"]
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-select'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["team_name", "logo", "color"]
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
        }