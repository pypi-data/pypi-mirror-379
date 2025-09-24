from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from users.models import User

def role_required(allowed_roles):
    """
    Decorator to restrict access based on user roles
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('users:login')
            
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied("You don't have permission to access this page.")
        return _wrapped_view
    return decorator

def admin_required(view_func):
    """
    Decorator to restrict access to Admin users only
    """
    return role_required([User.Role.ADMIN])(view_func)

def manager_required(view_func):
    """
    Decorator to restrict access to Manager and Admin users
    """
    return role_required([User.Role.ADMIN, User.Role.MANAGER])(view_func)

def auditor_required(view_func):
    """
    Decorator to restrict access to Auditor, Manager and Admin users
    """
    return role_required([User.Role.ADMIN, User.Role.MANAGER, User.Role.AUDITOR])(view_func)

def employee_required(view_func):
    """
    Decorator to restrict access to all authenticated users
    Since Employee is the base role, all users can access
    """
    return role_required([User.Role.ADMIN, User.Role.MANAGER, User.Role.AUDITOR, User.Role.EMPLOYEE])(view_func)