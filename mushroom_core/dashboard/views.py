# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import redirect

def dashboard_page(request):
	if not request.user.is_authenticated():
		return redirect('/login/')

	template = get_template('dashboard.html')
	variables = Context({
		'user': request.user,
		'request': request,
	})
	output = template.render(variables)
	return HttpResponse(output)
