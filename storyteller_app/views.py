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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            #return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
            try:
                intopk = Story.objects.get(pk=check_pk)
            except Story.DoesNotExist:
                intopk = Story.objects.order_by('-pk')[0]
            
            return HttpResponseRedirect("story",intopk.pk)
            #story_list = Story.objects.filter(post_id=check_pk).all()
            #post_story = Post.objects.get(pk=check_pk)
            #return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
        
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
    
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 9) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'storyteller_app/collection_e.html', {'contacts': contacts})
    
  
  
  
 
  
  
    
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
    
    Post.objects.filter(pk=temp_pk).update(post_likes = F('post_likes')+1)
    
    #return redirect("story",intopk.post_id)
    story_list = Story.objects.filter(post_id=temp_pk).all()
    post_story = Post.objects.get(pk=temp_pk)
    
        
    return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
 
 
 
    
    
def hot_sort(request):
    
    
    contact_list = Post.objects.all().order_by('-post_likes')
    paginator = Paginator(contact_list, 9) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'storyteller_app/collection_e.html', {'contacts': contacts})


    
    
    
    
    
def new_sort(request):
    
    contact_list = Post.objects.all().order_by('-pk')
    paginator = Paginator(contact_list, 9) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'storyteller_app/collection_e.html', {'contacts': contacts})
  
  
  
  
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

    

 