# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ta_app.models import Task, TaskDetail
from ta_app.form import TaskForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages

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

def update_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	form = TaskForm(request.POST or None, instance=task)
	if form.is_valid():
		form.save()
		return redirect('ta_app:task_list')
	return render(request, 'ta_app/task_form.html', {'form' : form})

def delete_task(request):
	print('delete_task activate')
	if request.method == 'POST':
		pk = request.POST.get('pk')
		print('in the post{}'.format(pk))
		task = get_object_or_404(Task, pk=pk)
		task.delete()
		return redirect('ta_app:task_list')
	return redirect('ta_app:task_list')

def report(request):
	users = User.objects.all()
	return render(request, 'ta_app/report.html', context={'users' : users}) 

def register(request):
	registered = False
	if request.method == 'POST':
		form = UserForm(request.POST or None)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			registered = True
			messages.success(request, '新增帳號成功')
			return redirect('ta_app:user_login')
		else:
			messages.add_message(request, 50, '無效的帳號或密碼')
	else:
		form = UserForm()
	
	return render(request,'ta_app/registration.html', context={
							'form' : form,
                           	'registered' : registered})


def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		
		if user and user.is_active :
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			messages.add_message(request, 50, '無效的帳號或密碼')

	return render(request, 'ta_app/user_login.html', {})

@login_required
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('user_login.html')
