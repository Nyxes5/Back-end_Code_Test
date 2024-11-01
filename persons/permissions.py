from rest_framework import permissions

class AdultPermission(permissions.BasePermission):

    message = "Person can't be under 18 years old."

    edit_methods = ("POST", "PUT", "PATCH")

    def has_permission(self, request, view):
        return (request.method not in self.edit_methods
                or int(request.data['age']) >= 18)