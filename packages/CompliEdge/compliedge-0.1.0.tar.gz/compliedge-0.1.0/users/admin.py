from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile, Team, TeamMembership, Company

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Fields',
            {
                'fields': (
                    'role',
                    'phone',
                    'department',
                    'position',
                    'mfa_enabled',
                )
            }
        )
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_code', 'created_by', 'created_at')
    search_fields = ('company_name', 'company_code')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'join_code', 'created_by', 'created_at')
    search_fields = ('name', 'join_code')
    list_filter = ('company',)

@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'is_owner', 'joined_at')
    search_fields = ('user__username', 'team__name')
    list_filter = ('is_owner', 'team__company')