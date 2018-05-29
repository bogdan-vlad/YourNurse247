from django.shortcuts import render

# Create your views here.
def home(request):
    """A view to home page"""
    return render(request, "home.html")

def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")
    
def about(request):
    """View of about page"""
    return render(request, 'about.html')
    
def contact(request):
    """View over the contact page"""
    return render(request, 'contact.html')