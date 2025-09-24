from users.models import User

def can_manage_users(user):
    """
    Check if user can manage users (Admin only)
    """
    return user.role == User.Role.ADMIN

def can_manage_policies(user):
    """
    Check if user can manage policies
    Admin: Full access
    Manager: Can create/edit within their scope
    Others: Read-only or no access
    """
    return user.role in [User.Role.ADMIN, User.Role.MANAGER]

def can_manage_compliance_frameworks(user):
    """
    Check if user can manage compliance frameworks (Admin only)
    """
    return user.role == User.Role.ADMIN

def can_define_risks(user):
    """
    Check if user can define risks
    Admin: Full access
    Manager: Can add risks
    Others: Read-only or no access
    """
    return user.role in [User.Role.ADMIN, User.Role.MANAGER]

def can_approve_workflows(user):
    """
    Check if user can approve workflows (Admin only)
    """
    return user.role == User.Role.ADMIN

def can_conduct_audits(user):
    """
    Check if user can conduct audits
    Admin, Manager, Auditor: Can conduct audits
    Employee: No access
    """
    return user.role in [User.Role.ADMIN, User.Role.MANAGER, User.Role.AUDITOR]

def can_submit_risk_observations(user):
    """
    Check if user can submit risk observations
    All authenticated users except Auditors can submit
    """
    return user.role in [User.Role.ADMIN, User.Role.MANAGER, User.Role.EMPLOYEE]

def can_acknowledge_policies(user):
    """
    Check if user can acknowledge policies
    All authenticated users can acknowledge
    """
    return True  # All authenticated users can acknowledge policies

def get_user_permissions(user):
    """
    Get all permissions for a user based on their role
    """
    permissions = {
        'can_manage_users': False,
        'can_manage_policies': False,
        'can_manage_compliance_frameworks': False,
        'can_define_risks': False,
        'can_approve_workflows': False,
        'can_conduct_audits': False,
        'can_submit_risk_observations': False,
        'can_acknowledge_policies': False,
        'is_read_only': False
    }
    
    if user.role == User.Role.ADMIN:
        # Admin has all permissions
        permissions = {key: True for key in permissions}
    elif user.role == User.Role.MANAGER:
        permissions.update({
            'can_manage_policies': True,
            'can_define_risks': True,
            'can_conduct_audits': True,
            'can_submit_risk_observations': True,
            'can_acknowledge_policies': True
        })
    elif user.role == User.Role.AUDITOR:
        permissions.update({
            'can_conduct_audits': True,
            'can_acknowledge_policies': True,
            'is_read_only': True
        })
    elif user.role == User.Role.EMPLOYEE:
        permissions.update({
            'can_submit_risk_observations': True,
            'can_acknowledge_policies': True
        })
    
    return permissions