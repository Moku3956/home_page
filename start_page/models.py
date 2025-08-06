from django.db import models

# Create your models here.
# class diplay(models.Model):

round_choices = [
        ('PRELIMINARY', '予選'),
        ('BEST16', 'Best16'),
        ('QUARTERFINAL', '準々決勝'),
        ('SEMIFINAL', '準決勝'),
        ('FINAL', '決勝'),
        ('OTHER', 'その他'),
    ]

class Result(models.Model):
    data = models.DateField()
    convention = models.CharField(max_length=100)
    round = models.CharField(
        choices= round_choices,
        default= 'PRELIMINARY'
    )
    opponent = models.CharField(max_length=50)
    score = models.CharField(max_length=10)
    comment = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.data} {self.convention} {self.get_round_display()}  vs{self.opponent}'