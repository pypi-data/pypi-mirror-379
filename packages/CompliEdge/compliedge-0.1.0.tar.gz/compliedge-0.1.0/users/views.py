from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, UserProfileForm, TeamForm, JoinTeamForm, AdminRegistrationForm
from .models import User, UserProfile, Company, Invitation, Team, TeamMembership
from permissions.decorators import admin_required
from permissions.utils import can_manage_users
from django.conf import settings

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard:home')
    
    def get_success_url(self):
        return reverse_lazy('dashboard:home')

class AdminLoginView(LoginView):
    template_name = 'users/admin_login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        # Get the user
        user = form.get_user()
        
        # Check if the user is an admin
        if user.role != User.Role.ADMIN:
            # Add an error message
            form.add_error(None, "Only admin users can access this portal.")
            return self.form_invalid(form)
        
        # If the user is an admin, proceed with login
        response = super().form_valid(form)
        
        # Set session timeout (30 minutes)
        self.request.session.set_expiry(1800)  # 30 minutes in seconds
        
        return response
    
    def get_success_url(self):
        return reverse_lazy('users:admin_dashboard')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'registration/password_reset_email.txt'
    subject_template_name = 'registration/password_reset_subject.txt'
    html_email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')

def register(request):
    # Check if the user is trying to register via invitation link
    invitation_token = request.GET.get('invitation_token')
    invitation = None
    
    if invitation_token:
        try:
            invitation = Invitation.objects.get(token=invitation_token)
            if not invitation.is_valid():
                messages.error(request, 'This invitation link has expired or is no longer valid.')
                invitation = None
        except Invitation.DoesNotExist:
            messages.error(request, 'Invalid invitation link.')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard:home')
    else:
        # Pre-fill company code if registering via invitation
        initial_data = {}
        if invitation:
            initial_data['company_code'] = invitation.company.company_code
        form = CustomUserCreationForm(initial=initial_data)
    
    return render(request, 'users/register.html', {
        'form': form,
        'invitation': invitation
    })


def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('secret_code')
            if code != settings.ADMIN_REGISTRATION_CODE:
                messages.error(request, 'Invalid admin registration code.')
            else:
                user = form.save()
                login(request, user)
                messages.success(request, 'Admin account created successfully!')
                return redirect('users:admin_dashboard')
    else:
        form = AdminRegistrationForm()
    return render(request, 'users/admin_register.html', { 'form': form })

def accept_invitation(request, token):
    """Accept an invitation link"""
    try:
        invitation = Invitation.objects.get(token=token)
    except Invitation.DoesNotExist:
        messages.error(request, 'Invalid invitation link.')
        return redirect('users:register')
    
    if not invitation.is_valid():
        messages.error(request, 'This invitation link has expired or is no longer valid.')
        return redirect('users:register')
    
    # Redirect to registration page with invitation token
    return redirect(f"{reverse_lazy('users:register')}?invitation_token={token}")

@login_required
def profile(request):
    try:
        profile = request.user.userprofile
    except ObjectDoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    profile_form = UserProfileForm(instance=profile)
    
    # Handle form submissions
    if request.method == 'POST':
        # Determine which form is being submitted
        if 'profile_submit' in request.POST:
            # Profile form submission
            profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('users:profile')
        elif 'user_submit' in request.POST:
            # User info form submission
            user = request.user
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.phone = request.POST.get('phone', user.phone)
            
            # Handle company code update (only for admin/manager)
            if request.user.role in [User.Role.ADMIN, User.Role.MANAGER]:
                company_code = request.POST.get('company_code')
                if company_code:
                    try:
                        company = Company.objects.get(company_code=company_code)
                        user.company = company
                    except Company.DoesNotExist:
                        messages.error(request, 'Invalid company code.')
                        return redirect('users:profile')
            
            user.save()
            messages.success(request, 'Your personal information has been updated!')
            return redirect('users:profile')
    
    return render(request, 'users/profile.html', {
        'profile_form': profile_form,
        'can_manage_users': can_manage_users(request.user)
    })

@admin_required
def user_list(request):
    """
    Display list of all users (Admin only)
    """
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@admin_required
def user_detail(request, pk):
    """
    Display user details (Admin only)
    """
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

@admin_required
def user_create(request):
    """
    Create a new user (Admin only)
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'User {user.username} created successfully!')
            return redirect('users:user_list')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Create User'})

@admin_required
def user_edit(request, pk):
    """
    Edit an existing user (Admin only)
    """
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        # For simplicity, we're not implementing a full user edit form here
        # In a real application, you would create a proper form for editing users
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.role = request.POST.get('role', user.role)
        
        # Handle company code update
        company_code = request.POST.get('company_code')
        if company_code:
            try:
                company = Company.objects.get(company_code=company_code)
                user.company = company
            except Company.DoesNotExist:
                messages.error(request, 'Invalid company code.')
                return redirect('users:user_edit', pk=pk)
        
        user.save()
        messages.success(request, f'User {user.username} updated successfully!')
        return redirect('users:user_list')
    
    return render(request, 'users/user_form.html', {
        'user': user,
        'title': 'Edit User',
        'roles': User.Role.choices
    })

@admin_required
def create_company(request):
    """
    Create a new company (Admin only)
    """
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        
        if company_name:
            try:
                company = Company.objects.create(
                    company_name=company_name,
                    created_by=request.user
                )
                # Generate an invitation link for the new company
                invitation_link = company.generate_invitation_link()
                messages.success(request, f'Company {company_name} created successfully with code: {company.company_code}')
                messages.info(request, f'Invitation link: {request.build_absolute_uri(invitation_link)}')
            except Exception as e:
                messages.error(request, f'Error creating company: {str(e)}')
        else:
            messages.error(request, 'Please provide a company name.')
        
        return redirect('users:create_company')
    
    # Generate a list of existing companies
    companies = Company.objects.all()
    return render(request, 'users/create_company.html', {'companies': companies})

@admin_required
def company_detail(request, pk):
    """
    View company details and generate invitation links (Admin only)
    """
    company = get_object_or_404(Company, pk=pk)
    
    # Get active invitations for this company
    invitations = company.invitations.filter(is_active=True).order_by('-created_at')
    
    if request.method == 'POST':
        # Generate a new invitation link
        invitation = Invitation.objects.create(company=company)
        invitation_link = request.build_absolute_uri(invitation.get_absolute_url())
        messages.success(request, f'New invitation link generated: {invitation_link}')
        return redirect('users:company_detail', pk=company.pk)
    
    return render(request, 'users/company_detail.html', {
        'company': company,
        'invitations': invitations
    })

@admin_required
def revoke_invitation(request, pk):
    """
    Revoke an invitation (Admin only)
    """
    invitation = get_object_or_404(Invitation, pk=pk)
    invitation.is_active = False
    invitation.save()
    messages.success(request, 'Invitation has been revoked.')
    return redirect('users:company_detail', pk=invitation.company.pk)

@admin_required
def admin_dashboard(request):
    """
    Admin dashboard with full system access
    """
    # Get system statistics
    total_users = User.objects.count()
    total_companies = Company.objects.count()
    total_active_invitations = Invitation.objects.filter(is_active=True).count()
    
    # Get recent users
    recent_users = User.objects.order_by('-date_joined')[:5]
    
    # Get recent companies
    recent_companies = Company.objects.order_by('-created_at')[:5]
    
    context = {
        'total_users': total_users,
        'total_companies': total_companies,
        'total_active_invitations': total_active_invitations,
        'recent_users': recent_users,
        'recent_companies': recent_companies,
    }
    
    return render(request, 'users/admin_dashboard.html', context)

@login_required
def delete_account(request):
    """
    Delete the user's account with confirmation
    """
    if request.method == 'POST':
        # Check if the user confirmed the deletion
        if request.POST.get('confirm') == 'yes':
            user = request.user
            username = user.username
            user.delete()
            messages.success(request, f'Account {username} has been successfully deleted.')
            return redirect('users:login')
        else:
            messages.info(request, 'Account deletion cancelled.')
            return redirect('users:profile')
    
    return render(request, 'users/delete_account.html')


@admin_required
def team_list(request):
    teams = Team.objects.filter(company__isnull=False)
    if request.user.company:
        teams = teams.filter(company=request.user.company)
    return render(request, 'users/team_list.html', { 'teams': teams })


@admin_required
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.company = request.user.company
            team.created_by = request.user
            team.save()
            TeamMembership.objects.create(user=request.user, team=team, is_owner=True)
            messages.success(request, 'Team created successfully')
            return redirect('users:team_detail', pk=team.pk)
    else:
        form = TeamForm()
    return render(request, 'users/team_form.html', { 'form': form })


@admin_required
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.user.company and team.company != request.user.company:
        messages.error(request, 'You do not have access to this team.')
        return redirect('users:team_list')
    members = User.objects.filter(team_memberships__team=team)
    # Users in same company not yet members (for assignment)
    available_users = User.objects.none()
    if request.user.role == User.Role.ADMIN and request.user.company:
        available_users = User.objects.filter(company=request.user.company).exclude(team_memberships__team=team)
    return render(request, 'users/team_detail.html', {
        'team': team,
        'members': members,
        'available_users': available_users,
    })


@admin_required
def team_add_member(request, pk, user_id):
    team = get_object_or_404(Team, pk=pk)
    user = get_object_or_404(User, pk=user_id)
    if request.user.company and (team.company != request.user.company or user.company != request.user.company):
        messages.error(request, 'Cross-company access denied.')
        return redirect('users:team_detail', pk=pk)
    TeamMembership.objects.get_or_create(user=user, team=team)
    messages.success(request, 'Member added to team.')
    return redirect('users:team_detail', pk=pk)


@admin_required
def team_remove_member(request, pk, user_id):
    team = get_object_or_404(Team, pk=pk)
    user = get_object_or_404(User, pk=user_id)
    TeamMembership.objects.filter(user=user, team=team).delete()
    messages.success(request, 'Member removed from team.')
    return redirect('users:team_detail', pk=pk)


@admin_required
def team_regenerate_code(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.user.company and team.company != request.user.company:
        messages.error(request, 'You do not have access to this team.')
        return redirect('users:team_list')
    team.join_code = ''
    team.save()
    messages.success(request, f'New team code generated: {team.join_code}')
    return redirect('users:team_detail', pk=pk)


@admin_required
def team_add_member_post(request, pk):
    """Assign a user to a team via POST (admin only)."""
    team = get_object_or_404(Team, pk=pk)
    if request.method != 'POST':
        return redirect('users:team_detail', pk=pk)
    user_id = request.POST.get('user_id')
    if not user_id:
        messages.error(request, 'Please select a user to add.')
        return redirect('users:team_detail', pk=pk)
    user = get_object_or_404(User, pk=user_id)
    if request.user.company and (team.company != request.user.company or user.company != request.user.company):
        messages.error(request, 'Cross-company access denied.')
        return redirect('users:team_detail', pk=pk)
    TeamMembership.objects.get_or_create(user=user, team=team)
    messages.success(request, 'Member added to team.')
    return redirect('users:team_detail', pk=pk)


@login_required
def join_team(request):
    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['join_code']
            try:
                team = Team.objects.get(join_code=code)
            except Team.DoesNotExist:
                messages.error(request, 'Invalid team code.')
                return redirect('users:join_team')
            if request.user.company and team.company != request.user.company:
                messages.error(request, 'Team belongs to a different company.')
                return redirect('users:join_team')
            # Align user's company if empty and safe to do so
            if request.user.company is None:
                request.user.company = team.company
                request.user.save()
            TeamMembership.objects.get_or_create(user=request.user, team=team)
            messages.success(request, f'Joined team {team.name}.')
            return redirect('users:team_detail', pk=team.pk)
    else:
        form = JoinTeamForm()
    return render(request, 'users/join_team.html', { 'form': form })