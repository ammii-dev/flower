from rest_framework import serializers

from core.models import Escort


class EscortsSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Escort
        fields = ('id', 'name', 'age')
        read_only_Fields = ('id')
