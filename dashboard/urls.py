from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('player/add', views.create_player, name='create_player'),
    path('team/add', views.create_team, name='create_team'),
]
