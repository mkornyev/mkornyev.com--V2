# IMPORTS 

from datetime import date, datetime, timezone 

from django.db import models
from django.contrib.auth.models import AbstractUser

class Project(models.Model):
	name = models.CharField(max_length=500, blank=False)
	short = models.TextField(max_length=500)
	content = models.TextField(max_length=900)
	date = models.DateTimeField(max_length=200, default=datetime.now(), blank=True)
	imageName = models.CharField(max_length=200, blank=True)
	tags = models.ManyToManyField('Tag')
	project_images = models.ManyToManyField('Image')

	class Meta:
		ordering = ['-date', 'name', 'content']

class Work(models.Model):
	name = models.CharField(max_length=500, blank=False)
	short = models.TextField(max_length=500)
	content = models.TextField(max_length=900)
	startDate = models.DateTimeField(max_length=200, default=datetime.now(), blank=False)
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
	userAgent = models.CharField(max_length=200, blank=True)
	fromPage = models.CharField(max_length=200, blank=True)

	datetime = models.DateTimeField(default=datetime.now())
	visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

	def __str__(self):
		return f"Visit to {self.path} by {self.visitor} on {self.datetime.month}/{self.datetime.day}/{str(self.datetime.year)[2:]} @{self.datetime.hour}:{self.datetime.minute}"
