from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from users.models import User

def company_required(view_func):
    """
    Decorator to restrict access based on company association
    User must be associated with a company to access the view
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return redirect('users:login')
        
        # Check if user is associated with a company
        if not request.user.company:
            raise PermissionDenied("You must be associated with a company to access this page.")
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def company_access_required(allowed_roles=None):
    """
    Decorator to restrict access based on both company association and role
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if user is authenticated
            if not request.user.is_authenticated:
                return redirect('users:login')
            
            # Check if user is associated with a company
            if not request.user.company:
                raise PermissionDenied("You must be associated with a company to access this page.")
            
            # If allowed_roles is specified, check user role
            if allowed_roles and request.user.role not in allowed_roles:
                raise PermissionDenied("You don't have permission to access this page.")
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def same_company_required(model_field='company'):
    """
    Decorator to ensure user can only access data from their own company
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if user is authenticated
            if not request.user.is_authenticated:
                return redirect('users:login')
            
            # Check if user is associated with a company
            if not request.user.company:
                raise PermissionDenied("You must be associated with a company to access this page.")
            
            # Check if the requested object belongs to the same company
            # This would typically be used with a specific object ID in the URL
            # For example: /policy/123/ where 123 is the policy ID
            # The view would need to verify that the policy belongs to the user's company
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator