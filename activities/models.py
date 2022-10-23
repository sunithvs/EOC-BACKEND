from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=150)
    description = RichTextField(blank=True, null=True)
    link = models.CharField(max_length=300, default='#')
    date = models.DateField(blank=True, null=True)
    image = models.FileField(blank=True, upload_to='programs/innovations/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Activities"
