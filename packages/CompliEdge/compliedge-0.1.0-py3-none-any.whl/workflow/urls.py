from django.urls import path
from . import views

app_name = 'workflow'

urlpatterns = [
    path('policies/<int:policy_id>/approve/', views.policy_approve, name='policy_approve'),
    path('policies/<int:policy_id>/approval/<int:approval_id>/', views.policy_approval_detail, name='policy_approval_detail'),
    path('risks/<int:risk_id>/approve/', views.risk_approve, name='risk_approve'),
    path('risks/<int:risk_id>/approval/<int:approval_id>/', views.risk_approval_detail, name='risk_approval_detail'),
    path('comments/add/', views.add_comment, name='add_comment'),
]