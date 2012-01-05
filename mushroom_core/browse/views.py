# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

@login_required
def browse_page(request):
	template = get_template('browse.html')
	variables = Context({
		'user': request.user,
		'request': request,
	})
	output = template.render(variables)
	return HttpResponse(output)
