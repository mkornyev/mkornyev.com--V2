from django.core.management.base import BaseCommand
from datetime import datetime
from mkv2.models import Project, ProjectScope, Tag, Image, Visitor, SiteVisit

# TEARDOWN SCRIPT

class Command(BaseCommand):
    args = '<this func takes no args>'
    help = 'Teardown script for projects / tags'

    def _destroyProjects(self):
        """
        sow = User.objects.create_user(username='sow', password='sow', first_name='Max', last_name='K', email='mkornyev@gmail.com')
        sow.is_staff = True 
        sow.is_superuser = False
        sow.save()
        """
        # Drop all objects:
        tagCnt = Tag.objects.count()
        Tag.objects.all().delete()

        projCnt = Project.objects.count()
        Project.objects.all().delete()

        imgCnt = Image.objects.count()
        Image.objects.all().delete()

        projSCnt = ProjectScope.objects.count()
        ProjectScope.objects.all().delete()

        print("{} Tags, {} Images, {} ProjectScopes, and {} Projects Deleted".format(tagCnt, imgCnt, projSCnt, projCnt))
    
    def _destroyVisitorData(self):
        visitorCnt = Visitor.objects.count()
        visitCnt = SiteVisit.objects.count()

        Visitor.objects.all().delete()
        SiteVisit.objects.all().delete()

        print("{} Visitors and {} Visits Deleted".format(visitorCnt, visitCnt))

    def handle(self, *args, **options):
        self._destroyProjects()
        # self._destroyVisitorData()