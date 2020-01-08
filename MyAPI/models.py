from django.db import models

# Create your models here.


class approvals(models.Model):
    Question = models.IntegerField()
    Clearmarks = models.IntegerField()
    Obtainmarks = models.FloatField()
    Time = models.FloatField()



    def __str__(self):
        return '{}, {}'.format(self.Question, self.Clearmarks)