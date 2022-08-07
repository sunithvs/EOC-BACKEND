from django.db import models
from django.db.models.base import Model

# Create your models here.

class Programs(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    ProgramName =models.CharField(max_length=100)
    ProgramDesc = models.CharField(max_length=1000)    
    ProgramDate = models.DateField()
    
    image = models.FileField(blank=True,upload_to='programs/images/')

    def __str__(self):
        return self.ProgramName

class PostImage(models.Model):
    post = models.ForeignKey(Programs, default=None, on_delete=models.CASCADE,related_name='imagges')
    images = models.FileField(upload_to = 'programs/images/',)
 
    def __str__(self):
        return self.post.ProgramName