# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from utils.scm_svn import MushroomScmSvn

@login_required
def browse_page(request, path):
	if path == None:
		path = ''
		path_str = '/'
	else:
		path_str = '/' + path
		
	filelist = []

	svn = MushroomScmSvn()
	svn.SVNGetFileListFolderAndRev(filelist, path, "HEAD")
	for file in filelist:
		if file.fd == 'F':
			file.name = file.path.split("/")[-1]
		else:
			file.name = file.path.split("/")[-2] + "/"
	
	split_path = path_str.split("/")
	split_path.pop()
	split_path.pop()
	parent_path = "/".join(split_path) + "/"
		
	template = get_template('browse.html')
	variables = Context({
		'path': path_str,
		'parent_path': parent_path,
		'filelist': filelist,
		'user': request.user,
		'request': request,
	})
	output = template.render(variables)
	return HttpResponse(output)
