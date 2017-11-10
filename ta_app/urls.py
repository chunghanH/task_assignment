from django.conf.urls import url, include
from . import views

app_name = 'ta_app'
urlpatterns = [
	url(r'^index/',views.index, name='index'),
	url(r'^task/',views.task, name='task'),
	url(r'^task_in_progress/',views.task_in_progress, name='task_in_progress'),
]