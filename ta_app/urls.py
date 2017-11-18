from django.conf.urls import url, include
from . import views

app_name = 'ta_app'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/', views.index, name='index'),
	url(r'^task/$', views.task_list, name='task_list'),
	url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
	url(r'^create/', views.create_task, name='create'),
	url(r'^update/(?P<pk>\d+)/$', views.update_task, name='update'),
	# url(r'^delete/(?P<pk>\d+)/$', views.delete_task, name='delete'),
	url(r'^delete/', views.delete_task, name='delete'),
	url(r'^report/', views.report, name='report'),
	url(r'^registration/', views.register, name='register'),
	url(r'^user_login/', views.user_login, name='user_login'),
	url(r'^user_logout/', views.user_logout, name='user_logout'),
]