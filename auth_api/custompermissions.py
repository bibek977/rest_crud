from rest_framework.permissions import BasePermission

class Mypermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return False
    

    # have to learn about this in brief
    def has_object_permission(self, request, view, obj):
        pass

    # Some third party permissions
    # DRF acess policy
    # Composed permissions
    # REST condition
    # DRY Rest permissions
    # Django rest framework roles
    # Django rest framework API key
    # Django rest framework Role filters
    # DRF PSQ