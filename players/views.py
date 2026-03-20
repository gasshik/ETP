from django.shortcuts import render
from .models import Player

def player_list(request):
    players = Player.objects.all().order_by('nickname')
    return render(request, 'players/player_list.html', {'players': players})
