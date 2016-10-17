from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): # this defines our model
	author = models.ForeignKey('auth.User') # this is a link to another model.
	title = models.CharField(max_length=500) # this is how you define text with a limited number of characters.
	text = models.TextField() # this is for long text without a limit. Sounds ideal for blog post content, right?
	created_date = models.DateTimeField(default=timezone.now) # this is a date and time.
	published_date = models.DateTimeField(blank=True, null=True)
	# More information around Django field types: https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-types

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
