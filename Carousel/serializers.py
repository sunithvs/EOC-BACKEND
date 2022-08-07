from rest_framework import serializers
from Carousel.models import carousel

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = carousel
        fields = ('Key','CarouselTittle','CarouselDesc','Carouselimage')
        