from django.contrib import admin

from .models import Player, Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_name", "logo", "team_country")
    search_fields = ("team_name", "team_country")
    list_filter = ("team_country",)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "nickname",
        "avatar",
        "first_name",
        "last_name",
        "date_of_birth",
        "rating",
        "team",
        "country",
    )
    search_fields = ("nickname", "first_name", "last_name")
    list_filter = ("team", "country")
