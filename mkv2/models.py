# IMPORTS 

from datetime import date, datetime, timezone 

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import tree


class ProjectScope(models.Model):
	name = models.CharField(max_length=10, blank=False)
	description = models.CharField(max_length=200, blank=False)
	token = models.CharField(max_length=1, blank=False)

	def __str__(self):
		return f'{self.scope} - {self.description}'
		
class Project(models.Model):
	name = models.CharField(max_length=500, blank=False)
	short = models.TextField(max_length=500)
	content = models.TextField(max_length=900)
	date = models.DateTimeField(max_length=200, default=datetime.now, blank=True)
	imageName = models.CharField(max_length=200, blank=True)
	tags = models.ManyToManyField('Tag')
	project_images = models.ManyToManyField('Image')
	
	scope = models.ForeignKey(ProjectScope, blank=True, null=True, on_delete=models.PROTECT)

	class Meta:
		ordering = ['-date', 'name', 'content']

	def __str__(self):
		return self.name

class Work(models.Model):
	name = models.CharField(max_length=500, blank=False)
	short = models.TextField(max_length=500)
	content = models.TextField(max_length=900)
	startDate = models.DateTimeField(max_length=200, default=datetime.now, blank=False)
	endDate = models.DateTimeField(max_length=200, blank=True)
	imageName = models.TextField(max_length=200, blank=True)
	tags = models.ManyToManyField('Tag')
	project_images = models.ManyToManyField('Image')

	class Meta:
		ordering = ['-startDate', 'name', 'content']

class Tag(models.Model):
	name = models.CharField(max_length=200, blank=False)

	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ['name']

class Image(models.Model):
	filename = models.CharField(max_length=200, blank=False)

	def __str__(self):
		return self.filename

# SITE VISITORS 

class Visitor(models.Model):
	ip = models.CharField(max_length=50, blank=False)
	alias = models.CharField(max_length=50, blank=True)
	ignoreVisits = models.BooleanField(default=False)
	# sitevisit_set

	def __str__(self):
		if self.alias:
			return f"{self.alias} | {self.ip}"
		else:
			return self.ip

class SiteVisit(models.Model):
	path = models.CharField(max_length=200, blank=False)
	meta = models.TextField(blank=True)
	cookies = models.TextField(blank=True)
	headers = models.TextField(blank=True)
	userAgent = models.TextField(blank=True)
	fromPage = models.TextField(blank=True)

	datetime = models.DateTimeField(default=datetime.now)
	visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

	def __str__(self):
		return f"Visit to {self.path} by {self.visitor} on {self.datetime.month}/{self.datetime.day}/{str(self.datetime.year)[2:]} @{self.datetime.hour}:{self.datetime.minute}"
