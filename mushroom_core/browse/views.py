# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from utils.scm_svn import MushroomScmSvn
from utils.relativeDates import timesince
import datetime

@login_required
def browse_page(request, path):
	if path == None:
		path = ''

	filelist = []

	svn = MushroomScmSvn()
	svn.LoadRootRevision()
	svn.SVNGetFileListFolderAndRev(filelist, path, "HEAD")

	for file in filelist:
		file.message = svn.GetCommitMsgByRev(file.rev)
		file.rev = "r" + file.rev
		file.date = datetime.datetime.strptime(file.date, "%Y-%m-%dT%H:%M:%S.%fZ")
		file.date = timesince(file.date)

		if file.fd == 'file':
			file.name = file.path.split("/")[-1]
		else:
			file.name = file.path.split("/")[-1] + "/"

		file.path = path + '/' + file.path
	
	split_path = path.split("/")
	if len(split_path) > 1:
		split_path.pop()
		split_path.pop()
		parent_path = "/".join(split_path) + "/"
	else:
		parent_path = ''
		
	template = get_template('browse.html')
	variables = Context({
		'path': path,
		'parent_path': parent_path,
		'filelist': filelist,
		'user': request.user,
		'request': request,
	})
	output = template.render(variables)
	return HttpResponse(output)
