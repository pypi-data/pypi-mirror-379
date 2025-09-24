from setuptools import setup, find_packages

setup(
    name="CompliEdge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Django>=4.2.0,<5.0.0",
        "Pillow>=9.0.0",
        "django-crispy-forms>=2.0.0",
        "crispy-tailwind>=0.6.0",
        "pyotp>=2.6.0",
        "qrcode>=7.3.1",
        "python-decouple>=3.6",
        "requests>=2.31.0"
    ],
    author="Rajesh Basnet",
    author_email="basnetrajesh245@gmail.com",
    description="CompliEdge - Enterprise GRC Management System",
    long_description="""CompliEdge is a cutting-edge, enterprise-grade GRC (Governance, Risk & Compliance)
management system built with Django and modern web technologies. The system provides comprehensive tools
for managing governance policies, identifying and mitigating risks, and ensuring compliance with
regulatory frameworks.

Key Features:
- User Management: Multi-role system with Admin, Manager, Employee, and Auditor roles
- Governance Module: Policy creation, approval, and publishing with versioning
- Risk Management: Risk identification, scoring, and mitigation strategies
- Compliance Management: Compliance frameworks and automated checklists
- Dashboard & Analytics: Interactive dashboards with real-time data visualization
- Notifications: Email and in-app notifications
- AI-Driven Insights: Predictive analytics for risk assessment
- Role-Based Access Control (RBAC): Fine-grained permissions for each user role
- Workflow Management: Multi-step approval processes for policies and risks
- Security Features: Two-factor authentication and comprehensive audit logs
- Collaboration Tools: Internal commenting system for policies, risks, and compliance items

Technologies Used:
- Backend: Django 4.x, Python 3.8+
- Frontend: HTML5, Tailwind CSS, JavaScript, Chart.js
- Database: SQLite (default), PostgreSQL (recommended for production)
- Authentication: Django's built-in authentication system
- Security: Two-factor authentication (pyotp, qrcode)
- AI/ML: Rule-based logic for risk prediction
- Static Files: Custom CSS and JavaScript
""",
    long_description_content_type="text/markdown",
    url="https://github.com/RajeshBasnet-dev/CompliEdge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
