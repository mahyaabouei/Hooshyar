from django.db import models
from django.utils import timezone
from Authentication.models import Consultant

class SelectTime(models.Model):
    date = models.DateTimeField(default=timezone.now)

    OPTION_STATUS = [
        ('assignment not determined', 'تعین تکلیف نشده'),
        ('cancel', 'لغو شده'),
        ('Reserv', 'رزرو'),
    ]
    status = models.CharField(max_length=100, choices=OPTION_STATUS)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} - {self.consultant}'

