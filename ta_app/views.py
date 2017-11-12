# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mylibrary.message import show_message
from ta_app.models import Task
# Create your views here.
def index(request):
	dics = {'content' : 'This is Index Page'}
	return render(request,'ta_app/index.html', context=dics)

def task(request):
	tasks = Task.objects.all()
	return render(request, 'ta_app/task.html', context={'tasks' : tasks})

def task_detail(request, pk):
	a_task = Task.objects.get(pk=pk)
	return render(request, 'ta_app/task_detail.html', context={'a_task' : a_task})

def report(request):
	dics = {'content' : 'This is report Page'}
	return render(request, 'ta_app/report.html', context=dics) 

def user_login(request):
	message = {}

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		
		if user and user.is_active :
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			message = show_message('red', '無效的帳號或密碼')
 
	return render(request, 'ta_app/user_login.html', context=message)

@login_required
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('user_login.html')