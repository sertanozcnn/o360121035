from re import search
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path,include
from appSale.models import housesale,Users,Price,House_Category
# def home(request):
#     return HttpResponse('<h1> Welcome to Home Page</h1>')




def index(request):
  house=housesale.objects.all()
  price=Price.objects.all()
  return render(request, 'index.html',{'house':house,'price':price}) 
def about(request):
  return render(request, 'about.html')
def house(request):
  house=housesale.objects.all()
  return render(request, 'house.html',{'house':house})
def price(request):
  price=Price.objects.all()
  return render(request, 'price.html',{'price':price})
def contact(request):
  return render(request, 'contact.html')


# def home(request):  
#     searchTerm = request.GET.get('searchMovie')
#     return render(request, 'home.html',{'searchTerm':searchTerm})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})




# Create your views here.
