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
			
			member1 = form.cleaned_data['member1']
			member2 = form.cleaned_data['member2']
			member3 = form.cleaned_data['member3']
			member4 = form.cleaned_data['member4']
			
			if member1 != "0":
				assign = Assign(issue_id=issue.id, user_id=member1)
				assign.save()
				
			if member2 != "0":
				assign = Assign(issue_id=issue.id, user_id=member2)
				assign.save()
				
			if member3 != "0":
				assign = Assign(issue_id=issue.id, user_id=member3)
				assign.save()
				
			if member4 != "0":
				assign = Assign(issue_id=issue.id, user_id=member4)
				assign.save()
			
			return HttpResponseRedirect('/issue')
		else:
			return HttpResponseRedirect('-')
			
	else:
		form = IssueCreateForm()

	return render_to_response('issue_create.html', {'form':form})
	
def issue_edit_page(request, issue_id):
	if not request.user.is_authenticated():
		return redirect('/login/')
	
	issue = Issue.objects.get(id=issue_id)
	
	data = {'name': issue.name, 
	'description': issue.description,
	'duedate': issue.duedate,
	'status': issue.status,
	'member1': 4,
	'member2': 1,
	'member3': 2,
	'member4': 3,}
	
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
			
			member1 = form.cleaned_data['member1']
			member2 = form.cleaned_data['member2']
			member3 = form.cleaned_data['member3']
			member4 = form.cleaned_data['member4']
						
			assign.user_id=member1
			assign.save()
			assign.user_id=member2
			assign.save()
			assign.user_id=member3
			assign.save()
			assign.user_id=member4
			assign.save()
			
			return HttpResponseRedirect('/issue')
			
		else:
			return HttpResponseRedirect('-')
			
	else:
		form = IssueCreateForm(data)

	return render_to_response('issue_edit.html', {'form':form})