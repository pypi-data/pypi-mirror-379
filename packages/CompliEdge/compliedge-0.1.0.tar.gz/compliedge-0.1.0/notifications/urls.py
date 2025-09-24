from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('send-test-email/', views.send_test_email_view, name='send_test_email'),
]