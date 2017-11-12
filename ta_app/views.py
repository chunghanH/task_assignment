# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mylibrary.message import show_message
from ta_app.models import Task, TaskDetail
from ta_app.form import TaskForm

# Create your views here.
def index(request):
	dics = {'content' : '歡迎使用派工系統'}
	return render(request,'ta_app/index.html', context=dics)

def task_list(request):
	tasks = Task.objects.all()
	return render(request, 'ta_app/task_list.html', context={'tasks' : tasks})

def task_detail(request, pk):
	task = Task.objects.get(pk=pk)
	return render(request, 'ta_app/task_detail.html', context={'task' : task})

def create_task(request):
	form = TaskForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('ta_app:task_list')
	return render(request, 'ta_app/task_form.html', {'form' : form, 'title' : '新增工作'})
# def update_task(request, pk):


# def delete_task(request, pk):


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