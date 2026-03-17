from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'first_name', 'last_name', 'age', 'rating')
    search_fields = ('nickname', 'first_name', 'last_name')