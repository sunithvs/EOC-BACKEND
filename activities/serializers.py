from rest_framework import serializers

from activities.models import Activity, ActivityImage


class ActivityImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    inoimages = ActivityImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = ["name", "short_desc", "description", "link", "date", "image", "inoimages"]
