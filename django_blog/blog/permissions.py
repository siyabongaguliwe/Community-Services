from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners or admins to access/edit objects.
    """

    def has_object_permission(self, request, view, obj):
        # Admins can access everything
        if request.user.is_staff:
            return True

        # Check ownership based on model type
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        elif hasattr(obj, 'provider'):
            return obj.provider == request.user
        elif hasattr(obj, 'organizer'):
            return obj.organizer == request.user
        elif hasattr(obj, 'user'):
            return obj.user == request.user

        return False
