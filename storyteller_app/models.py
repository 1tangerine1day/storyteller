from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Story(models.Model):
    
    context = models.CharField(max_length=100)
    time = models.CharField(max_length=25)
    auther = models.CharField(max_length=25)
    post_id = models.IntegerField(default=0)
    story_id = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
    	return self.context
    
    
class Post(models.Model):
	storyTitle = models.CharField(max_length=25)
	created_at = models.CharField(max_length=25)
	created_day = models.CharField(max_length=25)
	created_mon = models.CharField(max_length=25)
	post_likes = models.IntegerField(default=0)
	firstSentence = models.TextField(max_length=100)

	def __str__(self):
		return self.storyTitle
	

    