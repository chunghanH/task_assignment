# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
	user = models.OneToOneField(User)
	
	def __str__(self):
		return self.user.username

class Task(models.Model):
	subject = models.CharField(max_length=256)
	description = models.TextField(max_length=1024)
	reward = models.PositiveIntegerField()
	begin_date = models.DateField()
	number_of_people = models.PositiveIntegerField(default=1)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subject

class TaskDetail(models.Model):
	username = models.ForeignKey(User, related_name='tasks')
	task_pk =  models.ForeignKey(Task, related_name='tasks')

	def __str__(self):
		return self.task_pk.subject
