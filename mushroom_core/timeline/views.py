# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from utils.scm_svn import MushroomScmSvn
from utils.relativeDates import timesince
import datetime

@login_required
def timeline_page(request):
	svn = MushroomScmSvn()
	svn.LoadRootRevision()
	svnlogs = svn.svnLogList
	
	for log in svnlogs:
		#log.Date = datetime.datetime.strptime(log.Date, "%Y-%m-%dT%H:%M:%S.%fZ")
		#log.Date = timesince(log.Date) + " ago"
		for path in log.Paths:
			if path.action == 'A':
				path.action = "Added"
			elif path.action == 'D':
				path.action = "Deleted"
			else:
				path.action = "Modified"
		

	template = get_template('timeline.html')
	variables = Context({
		'user': request.user,
		'request': request,
		'svnlogs': svnlogs,
	})
	output = template.render(variables)
	return HttpResponse(output)
