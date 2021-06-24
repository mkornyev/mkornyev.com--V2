from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

from datetime import datetime
import requests

from mkv2.models import Project, Tag, Visitor, SiteVisit
from mkv2.forms import ProjectFilter

# CONSTANTS
 
KEYCDN_BASE_URL = 'https://tools.keycdn.com/geo.json'
CURRENT_HOST_URL = 'http://www.mkornyev.com'


# WRAPPERS 

def processRequest(func):
    def track(request):
        incomingIP = request.META.get("HTTP_X_FORWARDED_FOR", None)
        if not incomingIP: return

        newVisitor = Visitor.objects.filter(ip=incomingIP).first()

        if not newVisitor:
            newVisitor = Visitor(ip=incomingIP)
            newVisitor.save()
        else: 
            if newVisitor.ignoreVisits:
                return

        visit = SiteVisit(path=f'{request.scheme} {request.method} {request.path} {request.META.get("QUERY_STRING", "")}', 
            cookies=str(request.COOKIES), 
            headers=str(request.headers),
            userAgent=request.META.get("HTTP_USER_AGENT", "N/A"),
            fromPage=request.META.get("HTTP_REFERER", "N/A"),
            visitor=newVisitor)
        visit.meta = str(getCleanMeta(request.META))
        visit.save()
    
    def getCleanMeta(meta):
        fieldsToRemove = ["HTTP_X_FORWARDED_FOR","PATH_INFO","HTTP_COOKIE","QUERY_STRING","HTTP_REFERER","CSRF_COOKIE","CONTENT_LENGTH","CONTENT_TYPE","HTTP_HOST","HTTP_CONNECTION","HTTP_SEC_CH_UA","HTTP_SEC_CH_UA_MOBILE","HTTP_UPGRADE_INSECURE_REQUESTS","HTTP_USER_AGENT","HTTP_ACCEPT"]
        for f in fieldsToRemove:
            if f in meta: 
                del meta[f]
        return meta

    def wrapper(*args, **kwargs):
        try:
            track(args[0])
        except: 
            newVisitor = Visitor(ip='A SITEVISITOR ERROR HAS OCURRED')
            newVisitor.save()
        return func(*args, **kwargs)

    return wrapper


# VIEW FUNCTIONS 

@processRequest
def home(request):
    context = {}
    return render(request, 'mkv2/index.html', context)

@processRequest
def projects(request):
    allProjects = Project.objects.all()
    context = { 'filters': ProjectFilter(request.GET, queryset=allProjects) }

    if request.method == 'GET':
        query = request.GET.get('query')
        tags = request.GET.getlist('tags')
        context['projects'] = context['filters'].qs

        if query:
            context['projects'] = context['filters'].qs.filter( (Q(name__icontains=query) | (Q(short__icontains=query) | Q(content__icontains=query)) ))
            context['anchor'] = '#searchBar'
        elif tags:
            context['anchor'] = '#searchBar'

    return render(request, 'mkv2/projects.html', context)

@login_required
def fetchIpInfo(request):
    ip = request.GET.get('ip', None)
    if not ip: 
        return JsonResponse({'msg': 'No IP Passed'})

    if ip == '127.0.0.1' or ip == 'localhost':
      return JsonResponse({'msg':'Request not sent for local ip'})

    r = requests.get(f"{KEYCDN_BASE_URL}?host={ip}", headers={"User-Agent":f"keycdn-tools:{CURRENT_HOST_URL}"})
    if r.status_code == 200: 
      return JsonResponse(r.json())
    else:
      return JsonResponse({'msg': r.text})
