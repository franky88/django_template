from django.db import models

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=120)
	content=models.TextField()
	timestamp=models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="date published")
	updated=models.DateTimeField(auto_now=True, auto_now_add=False)
	def __unicode__(self):
		return self.title.upper()
	def __str__(self):
		return self.title.upper()
