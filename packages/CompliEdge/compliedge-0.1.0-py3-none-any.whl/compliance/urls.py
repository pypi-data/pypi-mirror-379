from django.urls import path
from . import views

app_name = 'compliance'

urlpatterns = [
    path('frameworks/', views.framework_list, name='framework_list'),
    path('frameworks/<int:pk>/', views.framework_detail, name='framework_detail'),
    path('checklists/', views.checklist_list, name='checklist_list'),
    path('checklists/<int:pk>/update/', views.checklist_update, name='checklist_update'),
    path('audits/', views.audit_list, name='audit_list'),
    path('audits/create/', views.audit_create, name='audit_create'),
    path('audits/<int:pk>/', views.audit_detail, name='audit_detail'),
]