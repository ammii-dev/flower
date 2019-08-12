from rest_framework import serializers

from core.models import Escort


class EscortsSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Escort
        fields = (
        'id', 
        'name', 
        'price', 
        'shape', 
        'height', 
        'height', 
        'gender', 
        'age', 
        'isVerified', 
        'image', 
        'contact_line', 
        'contact_phone', 
        'status', 
        'viewscount', 
        'zone', 
        'location', 
        'excerpt',
        'desc'
        )
        read_only_Fields = ('id')
