from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from mkv2.models import Project, Tag, Visitor, SiteVisit


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ("get_name", "get_short", "date")
  search_fields = ("name__icontains", "short__icontains")

  def get_name(self, obj):
    return format_html(obj.name)
  
  def get_short(self, obj):
    return format_html(obj.short)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
  list_display = ("ip", "alias", "ignoreVisits", "get_tot_visits", "get_last_visit", "get_ip_info")
  search_fields = ("ip__icontains", "alias__icontains")


  def get_tot_visits(self, obj):
    return SiteVisit.objects.all().filter(visitor=obj).count()
  get_tot_visits.short_description = "Tracked Visits"

  def get_last_visit(self, obj):
    return SiteVisit.objects.last().datetime
  get_last_visit.short_description = "Last Visit"

  def get_ip_info(self, obj):
    url = (reverse('IP Info') + '?' + urlencode({'ip': f'{obj.ip}'}))
    return format_html('<a href="{}">Fetch it!</a>', url)
  get_ip_info.short_description = "KeyCDN IP Info"
  
@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
  list_display = ("path", "visitor", "datetime", "fromPage", "userAgent")
  list_filter = ("datetime",)
  search_fields = ("path__icontains", "visitor__ip__icontains", "visitor__alias__icontains", "fromPage__icontains", "userAgent__icontains")
