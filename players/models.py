from django.db import models
from django_countries.fields import CountryField


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="teams/")
    team_flag = CountryField(blank_label="Оберіть країну", null=True, blank=True)
    color = models.CharField(max_length=10, default="#ffffff")
    team_country = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to="players/", null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.ForeignKey("Team", on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    flag = CountryField(blank_label="Оберіть країну", null=True, blank=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.nickname
