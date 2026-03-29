from django.shortcuts import render, redirect
from .forms import PlayerForm, TeamForm

def dashboard_home(request):
    return render(request, 'dashboard/home.html')

def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'dashboard/create_player.html', {'form': form})

def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = TeamForm()
    return render(request, 'dashboard/create_team.html', {'form': form})
    
    


