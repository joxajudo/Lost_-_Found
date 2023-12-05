from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.method in ['GET']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.user


class IsSenderOrReciever(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow access only if the requesting user is the sender or receiver of the message.
        return obj.sender == request.user or obj.receiver == request.user
