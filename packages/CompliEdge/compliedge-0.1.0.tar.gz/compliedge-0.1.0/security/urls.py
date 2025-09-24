from django.urls import path
from . import views

app_name = 'security'

urlpatterns = [
    path('audit-logs/', views.audit_log_list, name='audit_log_list'),
    path('2fa/setup/', views.two_factor_setup, name='two_factor_setup'),
    path('2fa/backup-codes/', views.two_factor_backup_codes, name='two_factor_backup_codes'),
    path('2fa/disable/', views.two_factor_disable, name='two_factor_disable'),
]