from django.db import models
from django.utils import timezone
from Authentication.models import Consultant

class SelectTime(models.Model):
    date = models.DateField()
    time = models.IntegerField()

    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} - {self.consultant}'

