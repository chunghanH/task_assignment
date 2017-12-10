# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


def get_name(self):
	return '{} {} {}'.format(self.user.last_name, self.user.first_name, self.user.username)

User.add_to_class('__str__', get_name)

# Create your models here.
class UserInfo(models.Model):
	user = models.OneToOneField(User)
	
class Task(models.Model):
	subject = models.CharField(max_length=256, verbose_name='主旨')
	description = models.TextField(max_length=1024, verbose_name='描述')
	reward = models.PositiveIntegerField(verbose_name='報酬')
	begin_date = models.DateField(verbose_name='派工日')
	number_of_people = models.PositiveIntegerField(default=1, verbose_name='人數')
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ManyToManyField(User)

	def __str__(self):
		return self.subject
