from re import search
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path,include

# def home(request):
#     return HttpResponse('<h1> Welcome to Home Page</h1>')




def index(request):
  return render(request, 'index.html')
def about(request):
  return render(request, 'about.html')
def house(request):
  return render(request, 'house.html')
def price(request):
  return render(request, 'price.html')
def contact(request):
  return render(request, 'contact.html')


# def home(request):  
#     searchTerm = request.GET.get('searchMovie')
#     return render(request, 'home.html',{'searchTerm':searchTerm})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})




# Create your views here.
