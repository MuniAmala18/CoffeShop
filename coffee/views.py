from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

# Create your views here.
def home(request):
    coffee = Coffee.objects.all()
    return render(request,'home.html',{'coffee':coffee})

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')