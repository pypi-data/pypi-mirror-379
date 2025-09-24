from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin

class CompanyAccessMiddleware:
    """
    Middleware to enforce company-based access control
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        # Define paths that require company association
        self.restricted_paths = [
            '/dashboard/',
            '/governance/',
            '/risk/',
            '/compliance/',
            '/ai/',
            '/workflow/',
            '/notifications/',
            '/security/',
        ]
        
        # Define paths that are always accessible (public paths)
        self.public_paths = [
            '/users/login/',
            '/users/register/',
            '/users/password_reset/',
            '/admin/',
        ]

    def __call__(self, request):
        # Check if the requested path requires company association
        path = request.path
        
        # Skip middleware for public paths
        if any(path.startswith(public_path) for public_path in self.public_paths):
            return self.get_response(request)
        
        # Skip middleware for static and media files
        if path.startswith('/static/') or path.startswith('/media/'):
            return self.get_response(request)
        
        # Check if user is authenticated
        if not request.user.is_authenticated:
            # Redirect to login for restricted paths
            if any(path.startswith(restricted_path) for restricted_path in self.restricted_paths):
                return redirect('users:login')
            return self.get_response(request)
        
        # Check if user is associated with a company for restricted paths
        if any(path.startswith(restricted_path) for restricted_path in self.restricted_paths):
            if not request.user.company:
                # Redirect to a page explaining they need to join a company
                # For now, we'll redirect to profile page with a message
                from django.contrib import messages
                messages.error(request, 'You must be associated with a company to access this page.')
                return redirect('users:profile')
        
        return self.get_response(request)