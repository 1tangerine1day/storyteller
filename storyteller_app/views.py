from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.
from .forms import AddForm, AddForm2
from .models import Story, Post
from django.http import HttpResponseRedirect
from time import localtime,strftime
from django.db.models import F

        


def show(request, pk):
    
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
            return render(request, 'storyteller_app/show.html',{'story': story_list, 'post': post_story})
            
        
        else:
            #return HttpResponseRedirect(request, 'mycontacts/show.html',{'story': story_list})   
            #url = reverse('story', kwargs={'story': check_pk})
            #return HttpResponseRedirect(url)
            story_list = Story.objects.filter(post_id=check_pk).all()
            post_story = Post.objects.get(pk=check_pk)
            return render(request, 'storyteller_app/show.html',{'story': story_list, 'post': post_story})
    
    else:
        story_list = Story.objects.filter(post_id=check_pk).all()
        post_story = Post.objects.get(pk=check_pk)
        return render(request, 'storyteller_app/show.html',{'story': story_list, 'post': post_story})
 
        
def likes(request, pk):
    
    temp_pk = pk
    
    Story.objects.filter(pk=temp_pk).update(likes = F('likes')+1)
    intopk = Story.objects.get(pk=temp_pk)
    
    #story_list = Story.objects.filter(post_id=1234).all()
    #return HttpResponseRedirect("url 'story' temp_pk")
    #return render_to_response('mycontacts/show.html',{'story': story_list})
    #url = reverse('story', kwargs={'story': temp_pk})
    #return HttpResponseRedirect(url)
    
    return redirect("story",intopk.post_id)
    
def collection_e(request):
    post_list = Post.objects.all()
    return render(request,'storyteller_app/collection_e.html',{
        'post_list': post_list,
    })
    
    
def collection_f(request):
    return render(request,'storyteller_app/collection_f.html')
    
    
def addpost(request):

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
            

        
            post_list = Post.objects.all()
            return redirect("story",intopk.pk)
        else:
            #return HttpResponseRedirect(request, 'mycontacts/show.html',{'story': story_list})   
            return HttpResponseRedirect("/")
    else:
        post_list = Post.objects.all()
        return render(request,'storyteller_app/collection_e.html',{'post': post_list})


def index(request):
    return render(request, 'storyteller_app/index.html')