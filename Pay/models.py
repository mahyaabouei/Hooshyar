from django.db import models
# from Visit.models import Visit

class Discount(models.Model):
    code = models.IntegerField()
    OPTION_KIND = [
        ('per', 'per'),
        ('val', 'val'),
    ]
    kind = models.CharField(max_length=10, choices=OPTION_KIND)
    expiration_date = models.DateTimeField()
    number_of_times = models.IntegerField()

    def __str__(self):
        return f'{self.code}'

# class Invoice (models.Model) :
#     '''
#     ForeignKey to Visit model
#     '''
#     pass




