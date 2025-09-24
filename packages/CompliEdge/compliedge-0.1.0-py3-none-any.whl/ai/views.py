from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .risk_predictor import RiskPredictor
from .compliance_checker import ComplianceChecker
from .models import ChatMessage, AISuggestion
from users.models import User
from .llm import generate_llm_response
from risk.models import Risk, RiskCategory
from governance.models import Policy
from compliance.models import ComplianceChecklist, ComplianceAudit

@login_required
def risk_predictions(request):
    """
    Display AI-driven risk predictions
    """
    # Get predictions
    predictions = RiskPredictor.predict_risks()
    compliance_risks = RiskPredictor.predict_policy_compliance_risks()
    
    return render(request, 'ai/risk_predictions.html', {
        'predictions': predictions,
        'compliance_risks': compliance_risks
    })

@login_required
def api_risk_predictions(request):
    """
    API endpoint for risk predictions (JSON response)
    """
    predictions = RiskPredictor.predict_risks()
    compliance_risks = RiskPredictor.predict_policy_compliance_risks()
    
    return JsonResponse({
        'risk_predictions': predictions,
        'compliance_risks': compliance_risks
    })

@login_required
def compliance_report(request):
    """
    Display automated compliance report
    """
    report = ComplianceChecker.get_compliance_report()
    
    return render(request, 'ai/compliance_report.html', {
        'report': report
    })

@login_required
def api_compliance_report(request):
    """
    API endpoint for compliance report (JSON response)
    """
    report = ComplianceChecker.get_compliance_report()
    
    # Convert datetime objects to strings for JSON serialization
    def serialize_policy_issue(issue):
        return {
            'policy_title': issue['policy'].title,
            'policy_id': issue['policy'].id,
            'days_overdue': issue['days_overdue'],
            'severity': issue['severity']
        }
    
    def serialize_checklist_issue(issue):
        return {
            'checklist_title': issue['checklist'].task,
            'checklist_id': issue['checklist'].id,
            'days_overdue': issue['days_overdue'],
            'severity': issue['severity']
        }
    
    def serialize_audit_issue(issue):
        return {
            'audit_title': issue['audit'].name,
            'audit_id': issue['audit'].id,
            'days_overdue': issue['days_overdue'],
            'severity': issue['severity']
        }
    
    serialized_report = {
        'compliance_score': report['compliance_score'],
        'overdue_policies': [serialize_policy_issue(issue) for issue in report['overdue_policies']],
        'overdue_checklists': [serialize_checklist_issue(issue) for issue in report['overdue_checklists']],
        'overdue_audits': [serialize_audit_issue(issue) for issue in report['overdue_audits']],
        'total_overdue_items': report['total_overdue_items']
    }
    
    return JsonResponse(serialized_report)

@method_decorator(login_required, name='dispatch')
class ChatbotView(View):
    """
    AI Chatbot interface
    """
    
    def get(self, request):
        """
        Render chatbot interface with chat history
        """
        # Get recent chat messages for this user
        chat_messages = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')[:20]
        chat_messages = reversed(chat_messages)  # Reverse to show oldest first
        
        return render(request, 'ai/chatbot.html', {
            'chat_messages': chat_messages
        })
    
    def post(self, request):
        """
        Handle chat message and generate AI response
        """
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)
            
            # Save user message
            chat_message = ChatMessage.objects.create(
                user=request.user,
                message=user_message,
                is_user_message=True
            )
            
            # Generate AI response
            ai_response = self.generate_response(user_message, request.user)
            
            # Save AI response
            ChatMessage.objects.create(
                user=request.user,
                message=user_message,
                response=ai_response,
                is_user_message=False
            )
            
            # Log the suggestion for auditing
            AISuggestion.objects.create(
                user=request.user,
                suggestion_type='chatbot_response',
                content=ai_response,
                context=f"User message: {user_message}"
            )
            
            return JsonResponse({
                'user_message': user_message,
                'ai_response': ai_response
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def generate_response(self, message, user):
        """
        Generate AI response based on user message and context
        """
        # Try free LLM first (if configured). Fallback to rules.
        system = (
            "You are CompliEdge AI assistant for a GRC platform. Be concise, cite app sections "
            "(Governance/Policies, Risk, Compliance) and suggest next actions."
        )
        llm_answer = generate_llm_response(message, system=system, max_tokens=200)
        if llm_answer:
            return llm_answer

        # Rule-based fallback
        message_lower = message.lower()
        
        # Handle greetings
        if any(greeting in message_lower for greeting in ['hello', 'hi', 'hey']):
            return "Hello! I'm your CompliEdge AI assistant. How can I help you with governance, risk, or compliance today?"
        
        # Handle policy questions
        if 'policy' in message_lower:
            policies = Policy.objects.filter(status='ACTIVE')[:3]
            if policies:
                policy_list = ', '.join([p.title for p in policies])
                return f"I found several active policies in our system: {policy_list}. You can view all policies in the Governance section."
            else:
                return "I couldn't find any active policies in the system. Please check the Governance section for more information."
        
        # Handle risk questions
        if 'risk' in message_lower:
            risks = Risk.objects.filter(status__in=['OPEN', 'IN_PROGRESS'])[:3]
            if risks:
                risk_list = ', '.join([r.title for r in risks])
                return f"There are currently open risks in our system: {risk_list}. You can view all risks in the Risk Management section."
            else:
                return "There are no currently open risks in the system. Great job on risk management!"
        
        # Handle compliance questions
        if 'compliance' in message_lower or 'checklist' in message_lower:
            overdue_items = ComplianceChecklist.objects.filter(
                status__in=['TODO', 'IN_PROGRESS'],
                due_date__lt=timezone.now().date()
            ).count()
            
            if overdue_items > 0:
                return f"There are {overdue_items} overdue compliance items that need attention. Please check the Compliance section for details."
            else:
                return "All compliance items are up to date. Great work on maintaining compliance!"
        
        # Handle general questions about the system
        if 'help' in message_lower:
            return ("I can help you with questions about policies, risks, and compliance. "
                   "Try asking about specific topics like 'What are our active policies?' "
                   "or 'Are there any open risks?'")
        
        # Default response
        return ("I'm your CompliEdge AI assistant. I can help you with governance, risk, and compliance questions. "
               "Try asking about policies, risks, or compliance items. For example: "
               "'What are our active policies?', 'Are there any open risks?', or 'Do we have any overdue compliance items?'")


@login_required
def ai_insights(request):
    """
    Summarize current risks, policies, and compliance with LLM; fallback to rule-based summary.
    """
    # Gather key context
    policies_active = Policy.objects.filter(status='ACTIVE')[:10]
    risks_open = Risk.objects.filter(status__in=['OPEN', 'IN_PROGRESS'])[:10]
    overdue_checklists = ComplianceChecklist.objects.filter(
        status__in=['TODO', 'IN_PROGRESS'],
        due_date__lt=timezone.now().date()
    )

    context_text = [
        f"Active policies: {', '.join(p.title for p in policies_active)}" if policies_active else "No active policies",
        f"Open risks: {', '.join(r.title for r in risks_open)}" if risks_open else "No open risks",
        f"Overdue compliance items: {overdue_checklists.count()}"
    ]
    prompt = (
        "Provide an executive GRC summary with 3 bullet insights and 3 recommended actions based on: "
        + " | ".join(context_text)
    )

    llm_summary = generate_llm_response(
        prompt,
        system=(
            "You summarize GRC posture for executives. Use short bullets (<=15 words). "
            "Be action-oriented and specific."
        ),
        max_tokens=220,
    )

    if not llm_summary:
        # Fallback concise summary
        insights = [
            "Policy coverage in place; review update cadence quarterly.",
            "Open risks require prioritization by impact and likelihood.",
            f"{overdue_checklists.count()} compliance items overdue; assign owners and due dates.",
        ]
        actions = [
            "Run quarterly policy reviews and approvals.",
            "Triage risks, assign owners, and set mitigation deadlines.",
            "Clear overdue compliance tasks; enable reminders and escalations.",
        ]
        llm_summary = "- " + "\n- ".join(insights) + "\n\nActions:\n- " + "\n- ".join(actions)

    return render(request, 'ai/insights.html', { 'summary': llm_summary })

@login_required
def get_chat_history(request):
    """
    API endpoint to get chat history for the current user
    """
    chat_messages = ChatMessage.objects.filter(user=request.user).order_by('-timestamp')[:20]
    chat_messages = reversed(chat_messages)  # Reverse to show oldest first
    
    messages = []
    for msg in chat_messages:
        messages.append({
            'message': msg.message,
            'response': msg.response,
            'timestamp': msg.timestamp.isoformat(),
            'is_user_message': msg.is_user_message
        })
    
    return JsonResponse({'messages': messages})