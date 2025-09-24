from django.db import models
from django.conf import settings
from datetime import datetime

class ChatMessage(models.Model):
    """
    Model to store chat messages between users and AI
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_chat_messages')
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_user_message = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"{self.user.username}: {self.message[:50]}..."

class AISuggestion(models.Model):
    """
    Model to store AI-generated suggestions for auditing purposes
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ai_suggestions')
    suggestion_type = models.CharField(max_length=50)  # e.g., 'risk_prediction', 'compliance_advice'
    content = models.TextField()
    context = models.TextField(blank=True)  # Additional context about the data used
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.suggestion_type}: {self.content[:50]}..."