from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'mkv2/index.html', context)

def projects(request):
    context = {}
    return render(request, 'mkv2/projects.html', context)