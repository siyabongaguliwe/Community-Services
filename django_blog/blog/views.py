from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Service, Event, Review
from .serializers import ListingSerializer, ServiceSerializer, EventSerializer, ReviewSerializer
from rest_framework import generics
from .permissions import IsOwnerOrAdmin
from .serializers import BusinessProfileSerializer
from .models import BusinessProfile

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Create your views here.
# views.py

class BusinessProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsOwnerOrAdmin]


class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsOwnerOrAdmin]
