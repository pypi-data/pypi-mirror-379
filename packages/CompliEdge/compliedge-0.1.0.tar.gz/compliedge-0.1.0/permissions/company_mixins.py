from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class CompanyRequiredMixin(LoginRequiredMixin):
    """
    Mixin to restrict access based on company association
    User must be associated with a company to access the view
    """
    
    def dispatch(self, request, *args, **kwargs):
        # Check if user is authenticated (handled by LoginRequiredMixin)
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        
        # Check if user is associated with a company
        if not request.user.company:
            raise PermissionDenied("You must be associated with a company to access this page.")
        
        return super().dispatch(request, *args, **kwargs)

class CompanyRoleRequiredMixin(CompanyRequiredMixin):
    """
    Mixin to restrict access based on both company association and role
    """
    allowed_roles = []
    
    def dispatch(self, request, *args, **kwargs):
        # Check company association (handled by CompanyRequiredMixin)
        if not request.user.is_authenticated or not request.user.company:
            return super().dispatch(request, *args, **kwargs)
        
        # Check if user has the required role
        if self.allowed_roles and request.user.role not in self.allowed_roles:
            raise PermissionDenied("You don't have permission to access this page.")
        
        return super().dispatch(request, *args, **kwargs)

class SameCompanyRequiredMixin(CompanyRequiredMixin):
    """
    Mixin to ensure user can only access data from their own company
    """
    model = None  # The model class to check against
    model_field = 'company'  # The field name for company in the model
    
    def dispatch(self, request, *args, **kwargs):
        # Check company association (handled by CompanyRequiredMixin)
        if not request.user.is_authenticated or not request.user.company:
            return super().dispatch(request, *args, **kwargs)
        
        # If we have a model and pk, check if the object belongs to the same company
        if self.model and 'pk' in kwargs:
            try:
                obj = self.model.objects.get(pk=kwargs['pk'])
                obj_company = getattr(obj, self.model_field, None)
                if obj_company != request.user.company:
                    raise PermissionDenied("You don't have permission to access this data.")
            except self.model.DoesNotExist:
                raise PermissionDenied("Data not found.")
        
        return super().dispatch(request, *args, **kwargs)