from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Home page view for CompliEdge landing page
    """
    return render(request, 'landing.html')