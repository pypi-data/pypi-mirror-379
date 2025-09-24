from django.urls import path
from . import views

app_name = 'risk'

urlpatterns = [
    path('', views.risk_list, name='risk_list'),
    path('risk/<int:pk>/', views.risk_detail, name='risk_detail'),
    path('risk/create/', views.risk_create, name='risk_create'),
    path('risk/<int:pk>/edit/', views.risk_edit, name='risk_edit'),
    path('risk/<int:risk_pk>/mitigation/create/', views.mitigation_create, name='mitigation_create'),
    path('predict/', views.risk_predict, name='risk_predict'),
]