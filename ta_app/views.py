# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ta_app.models import Task
from ta_app.form import TaskForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Avg, Sum

# Create your views here.
def index(request):
	dics = {'content' : '歡迎使用派工系統'}
	return render(request,'ta_app/index.html', context=dics)

def task_list(request):
	tasks = Task.objects.all()
	return render(request, 'ta_app/task_list.html', context={'tasks' : tasks})

@login_required
def task_detail(request, pk):
	task = Task.objects.get(pk=pk)

	return render(request, 'ta_app/task_detail.html', context={'task' : task})

@login_required
def create_task(request):
	form = TaskForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('ta_app:task_list')
	return render(request, 'ta_app/task_form.html', {'form' : form, 'title' : '新增工作'})

@login_required
def update_task(request, pk):
	task = get_object_or_404(Task, pk=pk)
	form = TaskForm(request.POST or None, instance=task)
	if form.is_valid():
		form.save()
		return redirect('ta_app:task_list')
	return render(request, 'ta_app/task_form.html', {'form' : form})

@login_required
def delete_task(request):
	if request.method == 'POST':
		pk = request.POST.get('pk')
		task = get_object_or_404(Task, pk=pk)
		task.delete()
		return redirect('ta_app:task_list')
	return redirect('ta_app:task_list')

@login_required
def join_task(request, pk):
	task = Task.objects.get(pk=pk)
	if task.user.all().count() < task.number_of_people:
		task.user.add(request.user)
		messages.success(request, '申請成功')
	else:
		messages.add_message(request, 50, '工作人數已滿')
	return redirect('ta_app:task_detail', pk)

@login_required
def unjoin_task(request, pk):
	task = Task.objects.get(pk=pk)
	task.user.remove(request.user)
	messages.success(request, '退出成功')
	return redirect('ta_app:task_detail', pk)
	
@login_required
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
			return redirect('ta_app:login')
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
