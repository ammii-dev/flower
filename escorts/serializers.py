from rest_framework import serializers
from escorts.models import EscortPost


class EscortSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscortPost
        fields = ('createdBy',
                'name',
                'awards',
                'age',
                'gender',
                'image',
                'tall',
                'weight',
                'lowest_price',
                'package',
                'body_ratio',
                'zone',
                'location',
                'description',
                'contactLine',
                'views_count',
                'isVerified',
                'isTopstar',
                'createdAt'
                )
