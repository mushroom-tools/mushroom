# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def join_member_page(request):
	template = get_template('join_member.html')
	variables = Context({
		'request': request,
	})
	output = template.render(variables)
	return HttpResponse(output)
