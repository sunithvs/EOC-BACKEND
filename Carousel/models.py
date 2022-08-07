from django.db import models

# Create your models here.
class carousel(models.Model):
    Key = models.AutoField(primary_key=True)
    CarouselTittle = models.CharField(max_length=100)
    CarouselDesc = models.CharField(max_length=200)
    Carouselimage = models.FileField(blank=True,upload_to='programs/carousel/')
   
    
    def __str__(self):
        return self.CarouselTittle