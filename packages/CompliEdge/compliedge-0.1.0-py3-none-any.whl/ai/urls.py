from django.urls import path
from . import views

app_name = 'ai'

urlpatterns = [
    path('risk-predictions/', views.risk_predictions, name='risk_predictions'),
    path('api/risk-predictions/', views.api_risk_predictions, name='api_risk_predictions'),
    path('compliance-report/', views.compliance_report, name='compliance_report'),
    path('api/compliance-report/', views.api_compliance_report, name='api_compliance_report'),
    path('chatbot/', views.ChatbotView.as_view(), name='chatbot'),
    path('api/chatbot/', views.ChatbotView.as_view(), name='api_chatbot'),
    path('api/chat-history/', views.get_chat_history, name='chat_history'),
    path('insights/', views.ai_insights, name='insights'),
]