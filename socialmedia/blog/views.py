from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'blog/index.html', {'option': 1})

def messages(request):
    return render(request, 'blog/index.html', {'option': 2})

def friends(request):
    return render(request, 'blog/index.html', {'option': 3})

def groups(request):
    return render(request, 'blog/index.html', {'option': 4})

def settings(request):
    return render(request, 'blog/index.html', {'option': 5})