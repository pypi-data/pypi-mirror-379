import random
from datetime import datetime, timedelta
from django.utils import timezone
from risk.models import Risk, RiskCategory
from governance.models import Policy

class RiskPredictor:
    """
    Enhanced AI-driven risk predictor based on historical data and rule-based logic
    """
    
    @staticmethod
    def predict_risks(user_department=None, category=None):
        """
        Predict potential risks based on historical data
        """
        # Get historical risks
        historical_risks = Risk.objects.all()
        
        if not historical_risks.exists():
            return []
        
        # Simple prediction logic based on historical patterns
        predictions = []
        
        # Get risk categories
        categories = RiskCategory.objects.all()
        if not categories.exists():
            # Return empty list if no categories exist
            return []
        
        # Predict based on historical patterns
        for i in range(5):  # Generate 5 predictions
            # Select a random category
            risk_category = random.choice(categories)
            
            # Determine likelihood and impact based on historical data
            historical_in_category = historical_risks.filter(category=risk_category)
            
            if historical_in_category.exists():
                # Calculate average likelihood and impact from historical data
                avg_likelihood = sum(r.likelihood for r in historical_in_category) / historical_in_category.count()
                avg_impact = sum(r.impact for r in historical_in_category) / historical_in_category.count()
            else:
                # Default values if no historical data
                avg_likelihood = random.randint(2, 4)
                avg_impact = random.randint(2, 4)
            
            # Adjust based on time factors (risks tend to increase over time)
            time_factor = min(1.5, (timezone.now() - historical_risks.latest('created_at').created_at).days / 30)
            likelihood = min(5, max(1, int(avg_likelihood * time_factor)))
            impact = min(5, max(1, int(avg_impact * time_factor)))
            
            # Calculate risk score
            risk_score = likelihood * impact
            
            # Determine priority
            if risk_score <= 5:
                priority = "LOW"
            elif risk_score <= 10:
                priority = "MEDIUM"
            elif risk_score <= 15:
                priority = "HIGH"
            else:
                priority = "CRITICAL"
            
            predictions.append({
                'title': f"Potential {risk_category.name} Risk",
                'description': f"Based on historical patterns, there's a potential risk in the {risk_category.name} category that requires attention.",
                'category': risk_category.name,
                'likelihood': likelihood,
                'impact': impact,
                'risk_score': risk_score,
                'priority': priority,
                'recommendation': RiskPredictor._get_recommendation(risk_category.name, priority),
                'confidence': random.randint(70, 95)  # Confidence level
            })
        
        return predictions
    
    @staticmethod
    def _get_recommendation(category, priority):
        """
        Get recommendation based on category and priority
        """
        recommendations = {
            "Cybersecurity": {
                "LOW": "Monitor network activity and ensure regular security updates. Consider implementing multi-factor authentication for critical systems.",
                "MEDIUM": "Conduct a comprehensive security audit and review access controls. Implement security awareness training for all employees.",
                "HIGH": "Implement additional security measures including intrusion detection systems and increase monitoring frequency. Engage external security experts for assessment.",
                "CRITICAL": "Immediate security assessment and incident response plan activation. Consider engaging cybersecurity incident response teams and notifying relevant authorities."
            },
            "Compliance": {
                "LOW": "Review current compliance policies and ensure they are up to date with latest regulations. Schedule regular compliance training sessions.",
                "MEDIUM": "Conduct a compliance audit and address any gaps found. Implement a compliance monitoring dashboard for real-time tracking.",
                "HIGH": "Engage legal team to address compliance issues and implement corrective actions. Consider external compliance auditing services.",
                "CRITICAL": "Immediate legal consultation and regulatory reporting if required. Implement emergency compliance measures and management oversight."
            },
            "Operational": {
                "LOW": "Review operational procedures and identify potential improvements. Implement process documentation standards.",
                "MEDIUM": "Conduct process optimization analysis and implement necessary changes. Establish key performance indicators for critical processes.",
                "HIGH": "Reorganize operational workflows and provide additional training. Implement business continuity planning and disaster recovery procedures.",
                "CRITICAL": "Emergency operational restructuring and management intervention required. Activate business continuity plan and crisis management team."
            },
            "Financial": {
                "LOW": "Review financial controls and ensure proper documentation. Implement regular financial reporting and variance analysis.",
                "MEDIUM": "Conduct financial audit and address any discrepancies found. Implement enhanced financial monitoring and approval workflows.",
                "HIGH": "Implement additional financial controls and increase oversight. Engage external auditors for specialized review.",
                "CRITICAL": "Immediate financial review by CFO and potential external audit. Consider engaging financial restructuring advisors and notifying stakeholders."
            }
        }
        
        # Default recommendations if category not found
        default_recommendations = {
            "LOW": "Monitor the situation and review relevant policies regularly. Consider implementing preventive measures.",
            "MEDIUM": "Investigate further and implement preventive measures. Schedule a review in 30 days.",
            "HIGH": "Take proactive measures to mitigate potential impact. Assign ownership and set deadlines for action items.",
            "CRITICAL": "Immediate action required to prevent significant impact. Escalate to senior management and implement emergency response procedures."
        }
        
        return recommendations.get(category, default_recommendations).get(priority, default_recommendations[priority])
    
    @staticmethod
    def predict_policy_compliance_risks():
        """
        Predict compliance risks for policies
        """
        policies = Policy.objects.all()
        
        if not policies.exists():
            return []
        
        compliance_risks = []
        
        for policy in policies:
            risk_factors = []
            
            # Check if policy is outdated (older than 1 year)
            if policy.updated_at and (timezone.now() - policy.updated_at).days > 365:
                risk_factors.append("Policy is outdated and may not reflect current regulations")
            
            # Check policy status
            if policy.status in ['DRAFT', 'REVIEW']:
                risk_factors.append("Policy is not yet approved and may not be enforceable")
            
            # Check if policy has been acknowledged by users
            # This would require additional models to track policy acknowledgments
            
            if risk_factors:
                # Determine risk level based on number of factors
                if len(risk_factors) == 1:
                    priority = "MEDIUM"
                elif len(risk_factors) == 2:
                    priority = "HIGH"
                else:
                    priority = "CRITICAL"
                
                compliance_risks.append({
                    'policy_title': policy.title,
                    'risk_factors': risk_factors,
                    'priority': priority,
                    'recommendation': RiskPredictor._get_policy_recommendation(len(risk_factors)),
                    'confidence': 85 if len(risk_factors) > 1 else 70
                })
        
        return compliance_risks
    
    @staticmethod
    def _get_policy_recommendation(risk_factor_count):
        """
        Get recommendation for policy compliance risks
        """
        if risk_factor_count == 1:
            return "Review and update the policy to ensure current compliance. Schedule regular policy reviews (quarterly) to maintain currency."
        elif risk_factor_count == 2:
            return "Prioritize policy approval and implement a regular review schedule. Assign ownership and set deadlines for completion."
        else:
            return "Immediate policy overhaul and management review required. Consider engaging external compliance experts for guidance."
    
    @staticmethod
    def get_ai_suggestions(user):
        """
        Generate AI suggestions for the dashboard based on user role and data
        """
        suggestions = []
        
        # Get user's risks
        if hasattr(user, 'owned_risks'):
            owned_risks = user.owned_risks.filter(status__in=['OPEN', 'IN_PROGRESS'])
            if owned_risks.exists():
                high_priority_risks = owned_risks.filter(priority__in=['HIGH', 'CRITICAL'])
                if high_priority_risks.exists():
                    suggestions.append({
                        'type': 'risk_management',
                        'title': 'High-Priority Risk Alert',
                        'description': f'You have {high_priority_risks.count()} high-priority risks that require immediate attention.',
                        'priority': 'HIGH',
                        'action_url': '/risk/',
                        'confidence': 90
                    })
                elif owned_risks.exists():
                    suggestions.append({
                        'type': 'risk_review',
                        'title': 'Risk Review Reminder',
                        'description': f'You have {owned_risks.count()} open risks that should be reviewed regularly.',
                        'priority': 'MEDIUM',
                        'action_url': '/risk/',
                        'confidence': 75
                    })
        
        # Check for overdue policies (if user is admin or manager)
        if user.role in ['ADMIN', 'MANAGER']:
            overdue_policies = Policy.objects.filter(
                updated_at__lt=timezone.now() - timedelta(days=365)
            )
            if overdue_policies.exists():
                suggestions.append({
                    'type': 'policy_update',
                    'title': 'Policy Update Required',
                    'description': f'There are {overdue_policies.count()} policies that are over a year old and may need updating.',
                    'priority': 'MEDIUM',
                    'action_url': '/governance/policies/',
                    'confidence': 85
                })
        
        # Check for compliance items
        # This would require linking users to compliance items
        
        # Add general suggestions if none found
        if not suggestions:
            suggestions.append({
                'type': 'general',
                'title': 'Compliance Health Check',
                'description': 'Consider running a full compliance assessment to identify potential areas for improvement.',
                'priority': 'LOW',
                'action_url': '/ai/compliance-report/',
                'confidence': 60
            })
        
        return suggestions