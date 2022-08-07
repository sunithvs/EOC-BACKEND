from rest_framework import serializers
from news.models import events

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = events
        fields = ('Key','EventName','EventDisc','EventDate','EventLink' )
        
         
    