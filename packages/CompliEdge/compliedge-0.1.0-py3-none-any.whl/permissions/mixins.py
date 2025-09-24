from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from users.models import User

class RoleRequiredMixin(LoginRequiredMixin):
    """
    Mixin to restrict access based on user roles for class-based views
    """
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if request.user.role in self.allowed_roles:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied("You don't have permission to access this page.")

class AdminRequiredMixin(RoleRequiredMixin):
    """
    Mixin to restrict access to Admin users only
    """
    allowed_roles = [User.Role.ADMIN]

class ManagerRequiredMixin(RoleRequiredMixin):
    """
    Mixin to restrict access to Manager and Admin users
    """
    allowed_roles = [User.Role.ADMIN, User.Role.MANAGER]

class AuditorRequiredMixin(RoleRequiredMixin):
    """
    Mixin to restrict access to Auditor, Manager and Admin users
    """
    allowed_roles = [User.Role.ADMIN, User.Role.MANAGER, User.Role.AUDITOR]

class EmployeeRequiredMixin(RoleRequiredMixin):
    """
    Mixin to restrict access to all authenticated users
    Since Employee is the base role, all users can access
    """
    allowed_roles = [User.Role.ADMIN, User.Role.MANAGER, User.Role.AUDITOR, User.Role.EMPLOYEE]