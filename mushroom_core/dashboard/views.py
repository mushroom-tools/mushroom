# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.conf import settings
from issues.models import Project
from issues.models import Issue

from utils.skype.SkypeApi import SkypeApi

@login_required
def dashboard_page(request):
	projects = Project.objects.order_by('-id')
	issues = Issue.objects.order_by('-id')
	template = get_template('dashboard.html')
	variables = Context({
		'user': request.user,
		'request': request,
		'projects': projects,
		'issues': issues,
	})
	output = template.render(variables)
	return HttpResponse(output)

def confcall(request):
	targets = request.REQUEST['targets'].split('|')
	if len(targets) > 0:
		api = SkypeApi(settings.SKYPE_USERNAME, settings.SKYPE_PASSWORD)
		api.call(targets)
