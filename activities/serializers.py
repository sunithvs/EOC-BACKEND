from rest_framework import serializers

from activities.models import Activity, ActivityImage


class ActivityImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    inoimages = ActivityImagesSerializer(many=True, read_only=True)
    InnovationID = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', "InnovationID", "name", "short_desc", "description", "link", "date", "image", "inoimages"]

    def get_InnovationID(self, obj):
        return obj.id
