from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile, Company, Team, TeamMembership

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=False)
    company_code = forms.CharField(max_length=50, required=True, 
                                  help_text="Enter your company's unique code")
    team_code = forms.CharField(max_length=10, required=True,
                                help_text="Enter the team code provided by your Admin")
    role = forms.ChoiceField(choices=[
        (User.Role.EMPLOYEE, 'Employee'),
        (User.Role.MANAGER, 'Manager')
    ], required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone", "company_code", "role", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the empty choice if it exists
        if hasattr(self.fields['role'], 'choices'):
            self.fields['role'].choices = [
                (User.Role.EMPLOYEE, 'Employee'),
                (User.Role.MANAGER, 'Manager')
            ]

    def clean_company_code(self):
        company_code = self.cleaned_data.get('company_code')
        try:
            company = Company.objects.get(company_code=company_code)
            return company
        except Company.DoesNotExist:
            raise forms.ValidationError("Invalid company code. Please contact your administrator.")
    
    def clean_team_code(self):
        team_code = self.cleaned_data.get('team_code')
        if not team_code:
            raise forms.ValidationError("Team code is required.")
        try:
            team = Team.objects.get(join_code=team_code)
        except Team.DoesNotExist:
            raise forms.ValidationError("Invalid team code. Please contact your administrator.")
        # Ensure company matches the provided company_code
        company = self.cleaned_data.get('company_code')
        if company and team.company_id != company.id:
            raise forms.ValidationError("Team code does not belong to the specified company.")
        return team
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone = self.cleaned_data["phone"]
        user.company = self.cleaned_data["company_code"]  # Company object from clean_company_code
        user.role = self.cleaned_data["role"]
        if commit:
            user.save()
            # Create team membership
            team = self.cleaned_data.get("team_code")
            if isinstance(team, Team):
                TeamMembership.objects.get_or_create(user=user, team=team)
        return user


class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    secret_code = forms.CharField(max_length=64, required=True, help_text="Enter the admin registration code")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "secret_code")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.role = User.Role.ADMIN
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'profile_picture']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description']


class JoinTeamForm(forms.Form):
    join_code = forms.CharField(max_length=10, label="Team Code")