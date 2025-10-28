from rest_framework import viewsets, generics
from .models import Listing, Service, Event, Review
from .serializers import (
    ListingSerializer,
    ServiceSerializer,
    EventSerializer,
    ReviewSerializer,
)
from .permissions import IsOwnerOrAdmin

# --- ViewSets for standard CRUD operations ---
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsOwnerOrAdmin]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsOwnerOrAdmin]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrAdmin]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrAdmin]

# --- Detail views with permission control ---


class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsOwnerOrAdmin]
