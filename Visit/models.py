from django.db import models
from django.utils import timezone
from Authentication.models import Auth, Consultant
# from Pay.models import Invoice
from django_summernote.fields import SummernoteTextField

class Question(models.Model):
    question = models.CharField(max_length=500)

class Visit(models.Model):
    customer = models.ForeignKey(Auth, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    cost = models.IntegerField()
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    survey = models.IntegerField(choices=RATING_CHOICES)
    # invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    note = SummernoteTextField()
    OPTION_Status = [
        ('completing', 'completing'),
        ('waiting', 'waiting'),
        ('done', 'done'),
        ('cancel', 'cancel'),
    ]
    status = models.CharField(max_length=20, choices=OPTION_Status)

    def __str__(self):
        return f'{self.customer} - {self.consultant}'

class KindOfCounseling(models.Model):
    title = models.CharField(max_length=100 , unique= True)
    price = models.IntegerField()
    icon = models.ImageField(upload_to='Hooshyar/Static/images/' , blank=True, null=True)