from django.core.management.base import BaseCommand
from datetime import datetime
from mkv2.models import Project, Tag

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

        print("{} Tags and {} Projects Deleted".format(tagCnt, projCnt))

    def handle(self, *args, **options):
        self._destroyProjects()