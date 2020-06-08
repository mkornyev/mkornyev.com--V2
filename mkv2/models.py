# IMPORTS 

from datetime import datetime 

from django.db import models
from django.contrib.auth.models import AbstractUser

class Project(models.Model):
	name = models.CharField(max_length=500, blank=False)
	short = models.TextField(max_length=500)
	content = models.TextField(max_length=900)
	date = models.DateTimeField(max_length=200, default=datetime.now(), blank=True)
	imageName = models.CharField(max_length=200, blank=True)
	tags = models.ManyToManyField('Tag')

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

	class Meta:
		ordering = ['-startDate', 'name', 'content']

class Tag(models.Model):
	name = models.CharField(max_length=200, blank=False)

	def __str__(self):
		return self.name

# class User(AbstractUser):
# 	created_at = models.DateTimeField(default=datetime.now())

# 	class Meta:
# 		ordering = ['first_name', 'last_name']
	
# 	def __str__(self):
# 		return self.get_username() + " (" + self.get_full_name() + ")"

# 	def print_attributes(self):
# 		print("---\nUsername: " + self.get_username() + "\nFirst name: " + self.first_name + "\nLast name: " + self.last_name + "\nEmail: " + self.email + "\nActive:" + str(self.is_active) + "\n---")