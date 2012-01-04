# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout

def main_page(request):
	if not request.user.is_authenticated():
		return redirect('/login/')
	else:
		return redirect('/dashboard/')

def logout_page(request):
	logout(request)
	return redirect('/')
