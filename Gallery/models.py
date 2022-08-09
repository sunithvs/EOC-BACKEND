from django.db import models
from django.db.models.base import Model


# Create your models here.

class Programs(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    ProgramName = models.CharField(max_length=100)
    ProgramDesc = models.CharField(max_length=100, default="", blank=True, null=True)
    ProgramDate = models.DateField(blank=True, null=True)
    long_desc = models.TextField(default="", blank=True, null=True)
    video = models.FileField(upload_to="videos")

    image = models.FileField(blank=True, upload_to='programs/images/')
    type = models.CharField(max_length=200, choices=(("EOC", "EOC"), ("SOCE", "SOCE")), default="EOC")

    def __str__(self):
        return self.ProgramName


class PostImage(models.Model):
    post = models.ForeignKey(Programs, default=None, on_delete=models.CASCADE, related_name='imagges')
    images = models.FileField(upload_to='programs/images/', )

    def __str__(self):
        return self.post.ProgramName


class Mentor(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=40)
    type = models.CharField(choices=(("Alumni", "Alumni"), ("Faculty", "Faculty"), ("Student", "Student")),
                            max_length=20)
    image = models.ImageField(upload_to="programs/images/")

    def __str__(self):
        return self.name
