from rest_framework.permissions import BasePermission

# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True
#         return False


# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         # Allow full CRUD for requests from the mobile app
#         # This example checks for a specific custom header. You should replace 'X-Mobile-App' and 'true' with your own logic.
#         if request.headers.get('X-Mobile-App') == 'true':
#             return True

#         # Allow read-only methods for others
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True

#         # Otherwise, deny permission
#         return False


# from rest_framework.permissions import BasePermission

# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         # Allow full CRUD for superusers
#         if request.user and request.user.is_authenticated and request.user.is_superuser:
#             return True

#         # Allow full CRUD for requests from the mobile app
#         if request.headers.get('X-Mobile-App') == 'true':
#             return True

#         # Allow read-only methods for others
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True

#         # Otherwise, deny permission
#         return False


from rest_framework.permissions import BasePermission

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow full CRUD for superusers
        if request.user and request.user.is_authenticated and request.user.is_superuser:
            return True

        # Allow full CRUD for requests from the mobile app
        if request.headers.get('X-Mobile-App') == 'true':
            return True

        # Deny access for all others
        return False