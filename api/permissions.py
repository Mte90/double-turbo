from rest_framework.permissions import BasePermission


class EndpointPermission(BasePermission):

    PUBLIC_PATHS = [
        '/auth/',
        '/register/',
    ]

    def has_permission(self, request, view):
        path = request.path
        if any(path.startswith(public_path) for public_path in self.PUBLIC_PATHS):
            return True
        return request.user and request.user.is_authenticated
