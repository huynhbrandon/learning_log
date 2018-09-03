from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry #import the model associated with topics from models.py
from .forms import TopicForm, EntryForm #import topicform class 

# Create your views here.
def index(request):
	"""The home page for learning log"""
	return render(request, 'learning_logs/index.html') #takes the request object and a template
	
@login_required #if unauthenticated, takes to LOGIN_URL
def topics(request):
	"""Show all topics"""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added') #sort the queryset
	# tells django to retrieve topic objects from db whose owner matches the current user
	
	context = {'topics': topics} #context is a dictionary where keys are names we use in templates
									#to access the data and the values are the data we need to send to the template
	return render(request, 'learning_logs/topics.html', context) #2nd argument is path to template

@login_required
def topic(request, topic_id): #second argument is the value captured by the regex storing a topic_id
	"""Show a single topic and all its entries."""
	topic = get_object_or_404(Topic, id=topic_id) #get specific topic - this is a query because they ask the db for info
	
	#Make sure the topic belongs to the current user.
	check_topic_owner(request, topic)
#	if topic.owner != request.user:
#		raise Http404
	
	entries = topic.entry_set.order_by('-date_added') #get entry associated with topic and reverse order them -  asks db for info so it's a query
	context = {'topic': topic, 'entries': entries} #makes available for templates to access the key names and values
	return render(request, 'learning_logs/topic.html', context) 

@login_required
def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted ; process data.
		form = TopicForm(request.POST)
		if form.is_valid():			# check if all fields are filled in
			new_topic = form.save(commit = False)
			new_topic.owner = request.user # value of owner field
			new_topic.save()		#writes data from form to db
			return HttpResponseRedirect(reverse('learning_logs:topics')) #take back to topics url 
			
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required	
def new_entry(request, topic_id):
	"""Add a new entry for a particular topic"""
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = EntryForm()
	else:
		#POST data submitted; process data
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False) #create a new entry object without saving it to db
			new_entry.topic = topic #set the entry to the specific topic model .topic() thanks to ForeignKey
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic_id])) #argument includes topic_id in the url
	
	context = {'topic': topic, 'form':form}
	return render(request, 'learning_logs/new_entry.html', context)
	
@login_required	
def edit_entry(request, entry_id):
	"""edit an existing entry."""
	entry = Entry.objects.get(id = entry_id) # get entry object user wants to edit
	topic = entry.topic
	check_topic_owner(request, topic)
#	if topic.owner != request.user:
#		raise Http404
	
	if request.method != 'POST':
		#initial request; pre-fill form with the current entry.
		form = EntryForm(instance = entry) #tells django to instantiate the prefilled info already in the entry object
	else:
		#POST data submitted; process data.
		form = EntryForm(instance = entry, data = request.POST) #tell Django to create a form instance based on pre-info and new
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic.id]))
	
	
	context = {'entry': entry, 'topic': topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)
	
def check_topic_owner(request, topic):
	if topic.owner != request.user:
		raise Http404
	
	
	
	
	
	
	