from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A model tells django how to work with the data that will be stored in the append
# basically a class

class Topic(models.Model):
	"""A topic the user is learning about"""
	text = models.CharField(max_length = 200) #used to store some text
	date_added = models.DateTimeField(auto_now_add=True) #auto sets time to this attribute
	owner = models.ForeignKey(User, on_delete = models.CASCADE) #using this key ID to connect topic to the user
									#establish a foreign key relationship to User model
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text
		
class Entry(models.Model):
	"""Something specific learned about a topic"""
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)		#reference to another record in the db; #django uses a key ID to connect two pieces of data
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		verbose_name_plural = 'entries'
	
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text[:50] + "..."