# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
import wall_model

@login_required
def wall_page(request):
	template = get_template('wall.html')
	logs = wall_model.get_transcript_all()
	
	variables = Context({
		'user': request.user,
		'request': request,
		'logs': logs,
	})
	output = template.render(variables)
	return HttpResponse(output)

def put_msg_to_db(request):
	name = request.REQUEST['name']
	content = request.REQUEST['content']
	wall_model.put_text(name, content)
	return HttpResponse('ok')
