from django.db import models
from django.contrib import admin

class Project(models.Model):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name
	
class AdminProject(admin.ModelAdmin):
	list_display = ("project", )
