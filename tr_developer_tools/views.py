"""
Views
"""
from django.shortcuts import render

def home(request):
    """
    Index
    """
    return render(request, 'index.html')
