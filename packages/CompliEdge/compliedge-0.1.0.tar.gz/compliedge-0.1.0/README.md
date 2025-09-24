# CompliEdge - Enterprise GRC Management System

CompliEdge is a cutting-edge, enterprise-grade GRC (Governance, Risk & Compliance) management system built with Django and modern web technologies. The system provides comprehensive tools for managing governance policies, identifying and mitigating risks, and ensuring compliance with regulatory frameworks.

## Key Features

- **User Management**: Multi-role system with Admin, Manager, Employee, and Auditor roles
- **Governance Module**: Policy creation, approval, and publishing with versioning
- **Risk Management**: Risk identification, scoring, and mitigation strategies
- **Compliance Management**: Compliance frameworks and automated checklists
- **Dashboard & Analytics**: Interactive dashboards with real-time data visualization
- **Notifications**: Email and in-app notifications
- **AI-Driven Insights**: Predictive analytics for risk assessment
- **Role-Based Access Control (RBAC)**: Fine-grained permissions for each user role
- **Workflow Management**: Multi-step approval processes for policies and risks
- **Security Features**: Two-factor authentication and comprehensive audit logs
- **Collaboration Tools**: Internal commenting system for policies, risks, and compliance items

## Technologies Used

- **Backend**: Django 4.x, Python 3.8+
- **Frontend**: HTML5, Tailwind CSS, JavaScript, Chart.js
- **Database**: SQLite (default), PostgreSQL (recommended for production)
- **Authentication**: Django's built-in authentication system
- **Security**: Two-factor authentication (pyotp, qrcode)
- **AI/ML**: Rule-based logic for risk prediction
- **Static Files**: Custom CSS and JavaScript

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CompliEdge
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Admin interface available at `http://127.0.0.1:8000/admin/`
- Login with the superuser credentials created in step 5

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.