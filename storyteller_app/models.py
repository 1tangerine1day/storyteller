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
    
class Post(models.Model):
	storyTitle = models.CharField(max_length=25)
	created_id = models.CharField(max_length=25)
	created_at = models.CharField(max_length=25)
	created_day = models.CharField(max_length=25)
	created_mon = models.CharField(max_length=25)
	post_likes = models.IntegerField(default=0)
	firstSentence = models.CharField(max_length=25)
	created_auther = models.CharField(max_length=25)
	
class Follow(models.Model):
	follow_post = models.CharField(max_length=25)
	follow_who = models.CharField(max_length=25)
	follow_created_at = models.CharField(max_length=25)
	follow_firstSentence = models.CharField(max_length=25)
	follow_storyTitle = models.CharField(max_length=25)

	


    