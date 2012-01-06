from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Issue(models.Model):
	user = models.ForeignKey(User)	
	name = models.CharField(max_length=200)	
	description = models.CharField(max_length=3000)
	date = models.DateTimeField(auto_now=True)
	duedate = models.DateTimeField(auto_now=False)
	status = models.BooleanField()
	
class Project(models.Model):
	name = models.CharField(max_length=200)	
	description = models.CharField(max_length=3000)
	date = models.DateTimeField(auto_now=True)
	
class Assign(models.Model):
	user = models.ForeignKey(User)
	issue = models.ForeignKey(Issue)
	
class Team(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
	
class CoWork(models.Model):
	user = models.ForeignKey(User)
	team = models.ForeignKey(Team)

class AdminIssue(admin.ModelAdmin):
	list_display = ("project", )
