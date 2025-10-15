from rest_framework import serializers
from .models import Listing, Service, Event, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# Note: BusinessProfile model/serializer removed because there is no
# BusinessProfile model defined in `blog/models.py`. If you add the model
# later, recreate this serializer accordingly.
