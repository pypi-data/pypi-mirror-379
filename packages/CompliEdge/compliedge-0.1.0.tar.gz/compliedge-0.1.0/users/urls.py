from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('admin/login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/register/', views.admin_register, name='admin_register'),
    path('accept_invitation/<str:token>/', views.accept_invitation, name='accept_invitation'),
    path('profile/', views.profile, name='profile'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('create_company/', views.create_company, name='create_company'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('revoke_invitation/<int:pk>/', views.revoke_invitation, name='revoke_invitation'),
    # Teams
    path('teams/', views.team_list, name='team_list'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),
    path('teams/<int:pk>/members/add/<int:user_id>/', views.team_add_member, name='team_add_member'),
    path('teams/<int:pk>/members/remove/<int:user_id>/', views.team_remove_member, name='team_remove_member'),
    path('teams/<int:pk>/regenerate_code/', views.team_regenerate_code, name='team_regenerate_code'),
    path('teams/<int:pk>/members/add/', views.team_add_member_post, name='team_add_member_post'),
    path('teams/join/', views.join_team, name='join_team'),
]