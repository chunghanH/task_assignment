# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	dics = {'content' : 'This is Index Page'}
	return render(request,'ta_app/index.html', context=dics)

def task(request):
	dics = {'content' : 'This is Task Page'}
	return render(request, 'ta_app/task.html', context=dics)

def task_in_progress(request):
	dics = {'content' : 'This is Task in Progress Page'}
	return render(request, 'ta_app/task_in_progress.html', context=dics)
