from django.db import models

# Create your models here.

class events(models.Model):
    Key = models.AutoField(primary_key=True)
    EventName = models.CharField(max_length=100)
    EventDisc = models.CharField(max_length=200)
    EventDate = models.DateField()
    EventLink = models.CharField(max_length=400)
    
    def __str__(self):
        return self.EventName