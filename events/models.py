from django.db import models
from django_countries.fields import CountryField


class Event(models.Model):
    EVENT_TYPES = [
        ('INTL', 'International LAN'),
        ('REG', 'Regional LAN'),
        ('ONL', 'Online'),
        ('MAJ', 'Major')
    ]
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    event_type = models.CharField(max_length=4, choices=EVENT_TYPES, default='ONL')
    start_date = models.DateField()
    end_date = models.DateField()
    prize_pool = models.CharField(max_length=100)
    team_count = models.IntegerField(default=16)
    logo = models.ImageField(upload_to="events_logo", blank=True, null=True)
    event_country = models.CharField(max_length=100)
    event_country_flag = CountryField(blank_label='Select a country', blank=True, null=True)


    class Meta:
        ordering = ["start_date"]
        verbose_name = "Турнір"
        verbose_name_plural = "Турніри"

    def __str__(self):
        return self.title
