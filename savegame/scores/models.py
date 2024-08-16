from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.score}"
