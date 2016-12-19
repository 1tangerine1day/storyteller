from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.
from .forms import AddForm, AddForm2, userForm
from .models import Story, Post, User
from django.http import HttpResponseRedirect
from time import localtime,strftime
from django.db.models import F

#global

    
        
def story(request, pk):
    
    check_pk = pk
    
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
            new_context = django_form.data.get("context")
            
            Story.objects.create(
                context =  new_context, 
                auther = "auther",
                time = strftime("%Y %b %d %X",localtime()),
                post_id = check_pk,
                likes = 0,
                )
                
            
            
            #url = reverse('story', kwargs={'story': check_pk})
            #return HttpResponseRedirect(url)
            story_list = Story.objects.filter(post_id=check_pk).all()
            post_story = Post.objects.get(pk=check_pk)
            #return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
            
            intopk = Story.objects.get(pk=check_pk)
            return redirect("story",intopk.post_id)
            
        
        else:
            #return HttpResponseRedirect(request, 'mycontacts/show.html',{'story': story_list})   
            #url = reverse('story', kwargs={'story': check_pk})
            #return HttpResponseRedirect(url)
            story_list = Story.objects.filter(post_id=check_pk).all()
            post_story = Post.objects.get(pk=check_pk)
            return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
    
    else:
        story_list = Story.objects.filter(post_id=check_pk).all()
        post_story = Post.objects.get(pk=check_pk)
        
        return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
 
 
 
 
 
 
 
        
def likes(request, pk):
    
    temp_pk = pk
    
    Story.objects.filter(pk=temp_pk).update(likes = F('likes')+1)
    intopk = Story.objects.get(pk=temp_pk)
    
    return redirect("story",intopk.post_id)
    
    
    
    
    
    
    
def collection_e(request):
    
    post_list  = Post.objects.all()
    
    return render(request,'storyteller_app/collection_e.html',{
        'post_list': post_list,
    })
    
  
  
  
 
  
  
    
def collection_f(request):
    
    return render(request,'storyteller_app/collection_f.html')
    
    
    
    
    
    
    
    
def addpost(request):
    
    post_list  = Post.objects.all()

    if request.method == 'POST':
        
        django_form = AddForm2(request.POST)
        if django_form.is_valid():
            new_title = django_form.data.get("new-title")
            first_sentence = django_form.data.get("first-sentence")
            
            Post.objects.create(
                storyTitle = new_title,
                created_at = strftime("%Y %b %d",localtime()),
                created_day = strftime("%d",localtime()),
                created_mon = strftime("%b",localtime()),
                post_likes = 0,
                firstSentence = first_sentence,
            )
            
            intopk = Post.objects.get(storyTitle=new_title)
            
            Story.objects.create(
                context =  first_sentence, 
                auther = "auther",
                time = strftime("%Y %b %d %X",localtime()),
                post_id = intopk.pk,
                likes = 0,
                )
            

            return redirect("story",intopk.pk)
        
        else:
            post_list  = Post.objects.all()
            return render(request,'storyteller_app/collection_e.html',{'post': post_list})
    
    else:
        post_list  = Post.objects.all()
        return render(request,'storyteller_app/collection_e.html',{'post': post_list})








def index(request):
    return render(request,'storyteller_app/index.html')
 
 
 
 
 
 
 
    

def post_likes(request, pk):
    
    temp_pk = pk
    
    Post.objects.filter(pk=temp_pk).update(post_likes = F('post_likes')+1)
    
    post_list  = Post.objects.all()
    
    
    return render(request, 'storyteller_app/collection_e.html',{'post_list': post_list })
    
   
   
def in_post_likes(request, pk):
    
    temp_pk = pk
    intopk = Story.objects.get(pk=temp_pk)
    
    Post.objects.filter(pk=temp_pk).update(post_likes = F('post_likes')+1)
    
    return redirect("story",intopk.post_id)
    
 
 
 
    
    
def hot_sort(request):
    
    
    post_list = Post.objects.all().order_by('-post_likes')
    
    return render(request, 'storyteller_app/collection_e.html',{'post_list': post_list})


    
    
    
    
    
def new_sort(request):
    
    post_list = Post.objects.all().order_by('-pk')
    
    return render(request, 'storyteller_app/collection_e.html',{'post_list': post_list})
    
  
  
  
  
  
def adduser(request):
    if request.method == 'POST':
        
        django_form = userForm(request.POST)
        if django_form.is_valid():
            
            new_name = django_form.data.get("name")
            new_account = django_form.data.get("account")
            new_password = django_form.data.get("password")
            
            User.objects.create(
                name = new_name,
                account = new_account,
                password = new_password,
            )

            return HttpResponseRedirect("/")
        
        else:
            return HttpResponseRedirect("/")
    
    else:
        return HttpResponseRedirect("/")

    