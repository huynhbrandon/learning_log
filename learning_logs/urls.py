"""Defines URL patterns for learning_logs."""

from django.urls import re_path, path

from . import views

app_name = 'learning_logs'
urlpatterns = [
	# home page
	re_path(r'^$', views.index, name = 'index'), # when a url matches the first argument, fx executes
	
	#Show all topics
	re_path(r'^topics/$', views.topics, name = 'topics'),
	
	#Detail page for a single topics
	re_path(r'^topics/(?P<topic_id>\d+)/', views.topic, name = 'topic'),
	
	#Page for adding a new topic
	re_path(r'^new_topic/$', views.new_topic, name = 'new_topic'),
	
	#Page for adding a new entry
	re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
	#matches any URL with the form http://localhost:8000/new_entry/id/ where id is matching topic ID
	
	# PAge for editing an entry
	re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),
	
	
	]
	
	
	