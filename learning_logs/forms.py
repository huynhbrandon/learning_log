from django import forms
from .models import Topic, Entry #import model classes

class TopicForm(forms.ModelForm):
	class Meta: #tell django to base the form off this simple form
		model = Topic
		fields = ['text']
		labels = {'text': ''}
		

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs = {'cols': 80})}