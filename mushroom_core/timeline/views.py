# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from dashboard.models import Project

@login_required
def timeline_page(request):
	projects = Project.objects.order_by('-id')
	template = get_template('timeline.html')
	variables = Context({
		'user': request.user,
		'request': request,
		'projects': projects,
	})
	output = template.render(variables)
	return HttpResponse(output)
