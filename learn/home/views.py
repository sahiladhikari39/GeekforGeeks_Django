from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    random_num = random.randint(100, 1000)
    context = {'random_num':random_num}
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def dynamic_url(request, id, id2):
    return render(request, 'home/dynamic_url.html', context={'id':id, 'id2':id2})