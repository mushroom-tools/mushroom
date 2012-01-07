from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
	user = models.ForeignKey(User)	
	name = models.CharField(max_length=200)	
	description = models.CharField(max_length=3000)
	date = models.DateTimeField(auto_now=True)
	duedate = models.DateTimeField(auto_now=False)
	status = models.BooleanField()

	def __unicode__(self):
		return name
	
class Team(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return name

class Project(models.Model):
	name = models.CharField(max_length=200)	
	description = models.CharField(max_length=3000)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return name
	
class Work(models.Model):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	
class Assign(models.Model):
	user = models.ForeignKey(User)
	issue = models.ForeignKey(Issue)
	
class CoWork(models.Model):
	user = models.ForeignKey(User)
	team = models.ForeignKey(Team)
	
