from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
    
def get_about(request):
    """View of about page"""
    return render(request, 'about.html')
    
def get_contact(request):
    """View over the contact page"""
    return render(request, 'contact.html')