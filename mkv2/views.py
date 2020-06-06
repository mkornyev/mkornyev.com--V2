from django.shortcuts import render
from mkv2.models import Project, Tag
from django.db.models import Q
from mkv2.forms import ProjectFilter

# Create your views here.

def home(request):
    context = {}
    return render(request, 'mkv2/index.html', context)

def projects(request):
    allProjects = Project.objects.all()
    context = { 'filters': ProjectFilter(request.GET, queryset=allProjects) }

    if request.method == 'GET':
        query = request.GET.get('query')

        if query:
            context['projects'] = context['filters'].qs.filter( (Q(name__icontains=query) | (Q(short__icontains=query) | Q(content__icontains=query)) ))
            context['anchor'] = '#searchBar'
        else: 
            context['projects'] = context['filters'].qs

    return render(request, 'mkv2/projects.html', context)