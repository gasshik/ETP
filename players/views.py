from django.shortcuts import render, get_object_or_404
from .models import Player

def player_list(request):
    select_country = request.GET.get('country')
    players = Player.objects.all().order_by('nickname')

    if select_country and select_country != 'All':
        players = players.filter(country=select_country)
    
    countries = Player.objects.values_list('country', flat=True).distinct()

    return render(request, 'players/player_list.html', {'players': players, 
        'countries': countries,
        'selected_country': select_country                                    
    })

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_detail.html', {'player': player})