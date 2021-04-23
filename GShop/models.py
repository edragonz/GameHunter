from django.db import models
from django.utils import timezone

# Create your models here.

class Game(models.Model):
    gameNo = models.AutoField(primary_key=True)
    gameName = models.CharField("game's name", max_length=50)
    gameInfo = models.TextField()
    gamePrice = models.DecimalField(max_digits=5, decimal_places=2)
    gameGenre = models.CharField("game's price", max_length=50)
    gameDeveloper = models.CharField("game's developer", max_length=50)
    gameReleaseDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.gameName
    