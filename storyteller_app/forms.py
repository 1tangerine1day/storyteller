from django import forms
from .models import Story,Post,Follow,Img
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _



class AddForm(forms.Form):
    
    class Meta:
        model = Story
        fields = ('context', 'time', 'auther', 'post_id', 'story_id', 'likes','auther_img')
	
class AddForm2(forms.Form):
    
    class Meta:
    	model = Post
    	fields = ('storyTitle', 'created_id', 'created_at', 'created_day', 'created_mon','post_likes', 'firstSentence','created_auther')
    	
    	
class FollowForm(forms.Form):
    
    class Meta:
    	model = Follow
    	fields = ('follow_post', 'follow_who', 'follow_created_id', 'follow_created_at', 'follow_likes', 'follow_firstSentence','follow_storyTitle',)
    	
class imgForm(forms.Form):
    
    class Meta:
    	model = Img
    	fields = ('username', 'img',)
  	

class RegistrationForm(forms.Form):
    
    username = forms.RegexField(regex=r'^\w+', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Account"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The account already exists. Please try another one."))
        
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
