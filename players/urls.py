from django.urls import path
from .views import player_list

urlpatterns = [
    path('', player_list, name='player_list'),
]