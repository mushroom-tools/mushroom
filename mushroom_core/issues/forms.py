from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxInput, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from issues.models import *

class IssueCreateForm(forms.Form):
	name = forms.CharField(label='Issue Name', max_length=200)
	description = forms.CharField(label='Description', max_length=3000, widget=forms.Textarea)
	duedate = forms.DateField(label='Due Date', widget=SelectDateWidget)
	status = forms.BooleanField(label='Opened', widget=CheckboxInput, required=False)
	member1 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))
	member2 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))
	member3 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))
	member4 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))
	
class IssueEditForm(forms.Form):
	name = forms.CharField(label='Issue Name', max_length=200)
	description = forms.CharField(label='Description', max_length=3000, widget=forms.Textarea)
	duedate = forms.DateField(label='Due Date', widget=SelectDateWidget)
	status = forms.BooleanField(label='Opened', widget=CheckboxInput, required=False)
	member1 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))
	member2 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))
	member3 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))
	member4 = forms.ChoiceField(widget=forms.Select, choices=(("0", "none"), ("1", "hana"), ("2", "jweb"), ("3", "kweb"), ("4", "yweb")))