from django.db.models import fields
from django.db.models.base import Model

from rest_framework import serializers
from Innovation.models import Innovation, InnovativeImages


class InnovativeImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InnovativeImages
        fields = '__all__'


class InnovationSerializer(serializers.ModelSerializer):
    inoimages = InnovativeImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Innovation
        fields = (
            "InnovationID", "name", "short_desc", "description", "link", "date", "image",'inoimages')
