from rest_framework import serializers
from .models import Venue


class VenueSerializer(serializers.ModelSerializer):
    schedules = serializers.StringRelatedField(many=True, read_only=True, )

    class Meta:
        model = Venue
        fields = (
            'name', 'address', 'description', 'stars',
            'cellphone', 'landline', 'booking_endpoint', 'website', 'schedules')
