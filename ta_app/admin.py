# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.

class TaskAdmin(admin.ModelAdmin):

	search_fields = ['subject','description','reward','begin_date','created_at','updated_at']
	list_filter = ['begin_date','created_at','updated_at']
	list_display = ['subject','description','reward','begin_date','created_at','updated_at']

admin.site.register(models.Task, TaskAdmin)
