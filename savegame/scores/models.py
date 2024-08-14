from django.db import models

class UserScore(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField()

    class Meta:
        db_table = 'users_scores'
        

    def __str__(self):
        return f'{self.username} - {self.score}'
