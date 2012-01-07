from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from issues.models import *
from issues.forms import *

def issues_page(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login/')

	issues = Issue.objects.order_by('-status')
	
	assigns = Assign.objects.filter(user=request.user)
	
	opened = Issue.objects.filter(status=True).count()
	closed = Issue.objects.filter(status=False).count()
	
	coworks = CoWork.objects.filter(user=request.user)
	teams = list()
	for cowork in coworks:
		teams.append(Team.objects.get(id=cowork.team_id))
	
	template = get_template('issues.html')
	variables = Context({
		'user': request.user,
		'request': request,
		'issues': issues,
		'assigns': assigns,
		'opened': opened,
		'closed': closed,
		'teams': teams,
	})
	output = template.render(variables)
	return HttpResponse(output)

def issue_project_page(request, issue_id):	
	return HttpResponse(output)
def issue_page(request, issue_id):
	template = get_template('issue.html')
	issue = Issue.objects.get(id=issue_id)
	username = User.objects.get(id=issue.user_id)
	assigns = Assign.objects.filter(issue=issue)
	variables = Context({
		'request': request,
		'issue': issue,
		'username': username,
		'assigns': assigns,
	})
	output = template.render(variables)
	return HttpResponse(output)

def issue_close_page(request, issue_id):
	issue = Issue.objects.get(id=issue_id)
	issue.status = 0
	issue.save()
	return HttpResponseRedirect('/issue/')
	
def issue_reopen_page(request, issue_id):
	issue = Issue.objects.get(id=issue_id)
	issue.status = 1
	issue.save()
	return HttpResponseRedirect('/issue/')
		
def issue_delete_page(request, issue_id):
	issue = Issue.objects.get(id=issue_id)
	issue.delete()
	return HttpResponseRedirect('/issue/')
	
def issue_create_page(request):	
	if not request.user.is_authenticated():
		return redirect('/login/')
	
	if request.method == 'POST':
	
		form = IssueCreateForm(request.POST)
		
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			user_id = request.user.id
			duedate = form.cleaned_data['duedate']
			status = form.cleaned_data['status']
			
			issue = Issue(name=name, description=description, user_id=user_id, duedate=duedate, status=status)
			issue.save()
			
			members = form.cleaned_data['members']
			members = members.split()
			
			for member in members:
				user = User.objects.get(username=member);
				assign = Assign(user=user, issue=issue)
				assign.save()
				
			return HttpResponseRedirect('/issue')
		else:
			return HttpResponseRedirect('-')
			
	else:
		users = User.objects.all()
		cowork = CoWork.objects.get(user = request.user)
		cws = CoWork.objects.filter(team = cowork.team)
		
		members = ''
		for cw in cws:
			members += cw.user.username
			members += ' '
		
		data = {'members': members}
		form = IssueCreateForm(data)

	return render_to_response('issue_create.html', {'form':form})
	
def issue_edit_page(request, issue_id):
	if not request.user.is_authenticated():
		return redirect('/login/')
	
	issue = Issue.objects.get(id=issue_id)
	
	assigns = Assign.objects.filter(issue=issue)
	members = ''
	for assign in assigns:
		members += assign.user.username
		members += ' '
		
	data = {'name': issue.name, 
	'description': issue.description,
	'duedate': issue.duedate,
	'status': issue.status,
	'members': members}
	
	if request.method == 'POST':
		form = IssueCreateForm(request.POST)
		
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			user_id = request.user.id
			duedate = form.cleaned_data['duedate']
			status = form.cleaned_data['status']
			
			issue.name=name
			issue.description=description
			issue.user_id=user_id
			issue.duedate=duedate
			issue.status=status
			issue.save()
			
			members = form.cleaned_data['members']
			members = members.split()
			
			assigns = Assign.objects.filter(issue=issue)
			for assign in assigns:
				assign.delete()
			
			members = form.cleaned_data['members']
			members = members.split()
			
			for member in members:
				user = User.objects.get(username=member);
				assign = Assign(user=user, issue=issue)
				assign.save()
			
			return HttpResponseRedirect('/issue')
			
		else:
			return HttpResponseRedirect('-')
			
	else:
		form = IssueCreateForm(data)

	return render_to_response('issue_edit.html', {'form':form})