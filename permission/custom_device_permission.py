from rest_framework import permissions

class DevicePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        user_role = request.user.user_role

        # Owners can delete or modify the device
        if user_role == "OR":
            return True

        # Engineers and Managers can update and view devices
        if user_role in ["ER", "MR"]:
            return request.method in permissions.SAFE_METHODS + ("PUT",)

        # Editors can only view devices
        if user_role == "OP":
            return request.method in permissions.SAFE_METHODS

        return False
