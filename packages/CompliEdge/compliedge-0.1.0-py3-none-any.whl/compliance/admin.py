from django.contrib import admin
from .models import ComplianceFramework, ComplianceRequirement, ComplianceChecklist, ComplianceAudit

@admin.register(ComplianceFramework)
class ComplianceFrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'description')
    search_fields = ('name', 'abbreviation')

@admin.register(ComplianceRequirement)
class ComplianceRequirementAdmin(admin.ModelAdmin):
    list_display = ('framework', 'clause', 'title')
    list_filter = ('framework',)
    search_fields = ('clause', 'title', 'description')

@admin.register(ComplianceChecklist)
class ComplianceChecklistAdmin(admin.ModelAdmin):
    list_display = ('requirement', 'assigned_to', 'status', 'due_date')
    list_filter = ('status', 'due_date', 'requirement__framework')
    search_fields = ('requirement__title', 'assigned_to__username')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(ComplianceAudit)
class ComplianceAuditAdmin(admin.ModelAdmin):
    list_display = ('framework', 'auditor', 'audit_date', 'completed')
    list_filter = ('framework', 'completed', 'audit_date')
    search_fields = ('findings', 'recommendations')
    readonly_fields = ('created_at',)