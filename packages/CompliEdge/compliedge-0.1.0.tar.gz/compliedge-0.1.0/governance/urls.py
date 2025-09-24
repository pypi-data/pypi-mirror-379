from django.urls import path
from . import views

app_name = 'governance'

urlpatterns = [
    path('', views.policy_list, name='policy_list'),
    path('policy/<int:pk>/', views.policy_detail, name='policy_detail'),
    path('policy/create/', views.policy_create, name='policy_create'),
    path('policy/<int:pk>/edit/', views.policy_edit, name='policy_edit'),
    path('document/<int:pk>/download/', views.policy_document_download, name='policy_document_download'),
]