from django.db import models

# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    descriptions = models.TextField()
    age = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nickname