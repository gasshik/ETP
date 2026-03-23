from django.shortcuts import render, get_object_or_404
from .models import Player

def player_list(request):
    players = Player.objects.all().order_by('nickname')
    return render(request, 'players/player_list.html', {'players': players})

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_detail.html', {'player': player})