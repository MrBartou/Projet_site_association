from rest_framework.permissions import *


class AllowGuestPostOnly(BasePermission):
    """
    Custom permissions to allow guest to use specified permissions.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        return bool(request.user and request.user.is_authenticated)
