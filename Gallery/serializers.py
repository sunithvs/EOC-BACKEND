from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from Gallery.models import Programs, PostImage, Mentor


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    imagges = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Programs
        fields = ("ProgramID", "ProgramName", "ProgramDesc", "ProgramDate", "image", 'imagges')


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
