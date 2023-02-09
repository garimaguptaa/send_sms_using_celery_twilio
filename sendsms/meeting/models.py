from django.db import models

# Create your models here.
class Meeting(models.Model):
    phone_number = models.CharField(max_length=20)
    date_time = models.DateTimeField()


    def __str__(self) -> str:
        return self.phone_number