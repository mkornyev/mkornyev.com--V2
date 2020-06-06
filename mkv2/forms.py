from django import forms
from django.contrib.auth import authenticate
from django.db import models
from mkv2.models import *
import django_filters

class ProjectFilter(django_filters.FilterSet):
	tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, label='')

	class Meta:
		model = Project
		fields = ('tags',)