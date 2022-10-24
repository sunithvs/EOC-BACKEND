from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField


# Create your models here.

class Innovation(models.Model):
    InnovationID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=150)
    description = RichTextField(blank=True, null=True)
    link = models.CharField(max_length=300, default='#')
    InnovationYBLink = models.CharField(max_length=200, default='#')
    date = models.DateField(blank=True, null=True)

    image = models.FileField(blank=True, upload_to='programs/innovations/')

    def __str__(self):
        return self.name


class InnovativeImages(models.Model):
    InoIMG = models.ForeignKey(Innovation, default=None, on_delete=models.CASCADE, related_name='inoimages')
    images = models.FileField(upload_to='programs/innovations/', )

    def __str__(self):
        return self.InoIMG.name
