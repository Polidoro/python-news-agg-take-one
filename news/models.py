from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Feed(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(unique=True)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Article(models.Model):
	feed = models.ForeignKey(Feed)
	title = models.CharField(max_length=200)
	url = models.URLField(unique=True)
	description = models.TextField()
	publication_date = models.DateTimeField()

	def __str__(self):
		return self.title