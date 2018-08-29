from django.contrib import admin

from learning_logs.models import Topic, Entry #class
# Register your models here.

admin.site.register(Topic) # tell django to manager our model through admin site
admin.site.register(Entry) # tell django to manage our entry model