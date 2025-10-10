from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, ServiceViewSet, EventViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'events', EventViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
