from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    random_num = random.randint(100, 1000)
    fruits = ["Banana 🍌", "Apple 🍎", "Grapes 🍇"]
    countries = [
    {"name": "Nepal", "capital": "Kathmandu", "continent": "Asia"},
    {"name": "India", "capital": "New Delhi", "continent": "Asia"},
    {"name": "United States", "capital": "Washington, D.C.", "continent": "North America"},
    {"name": "Germany", "capital": "Berlin", "continent": "Europe"},
    {"name": "Brazil", "capital": "Brasília", "continent": "South America"},
    {"name": "Australia", "capital": "Canberra", "continent": "Australia"},
    {"name": "Egypt", "capital": "Cairo", "continent": "Africa"},
    {"name": "Canada", "capital": "Ottawa", "continent": "North America"},
    {"name": "France", "capital": "Paris", "continent": "Europe"},
    {"name": "Japan", "capital": "Tokyo", "continent": "Asia"}
    ]
    context = {'random_num':random_num, "fruits":fruits, 'countries':countries}
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def dynamic_url(request, id, id2):
    return render(request, 'home/dynamic_url.html', context={'id':id, 'id2':id2})


def project(request):
    ranNum= random.randint(1, 10)
    context={'ranNum':ranNum}
    return render(request, 'project/project.html', context)