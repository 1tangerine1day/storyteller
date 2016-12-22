from django import forms
from .models import Story,Post,User

class AddForm(forms.Form):
    
    class Meta:
        model = Story
        fields = ('context', 'time', 'auther', 'post_id', 'story_id', 'likes',)
	
class AddForm2(forms.Form):
    
    class Meta:
    	model = Post
    	fields = ('storyTitle', 'create_id', 'created_at', 'created_day', 'created_mon','post_likes', 'firstSentence',)

class userForm(forms.Form):
    
    class Meta:
    	model = User
    	fields = ('name', 'account', 'password',)
