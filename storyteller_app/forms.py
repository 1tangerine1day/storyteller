from django import forms
from .models import Story,Post

class AddForm(forms.Form):
    
    class Meta:
        model = Story
        fields = ('context', 'time', 'auther', 'post_id', 'story_id', 'likes',)
	
class AddForm2(forms.Form):
    
    class Meta:
    	model = Post
    	fields = ('storyTitle', 'created_at', 'firstSentence',)
