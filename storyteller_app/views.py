from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.
from .forms import AddForm, AddForm2, RegistrationForm, User
from .models import Story, Post
from django.http import HttpResponseRedirect
from time import localtime,strftime
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth import logout
import time


def story(request, pk):
    
    check_pk = pk
    if request.method == 'POST':
        django_form = AddForm(request.POST)
        if django_form.is_valid():
            new_context = django_form.data.get("context")
            
            Story.objects.create(
                context =  new_context, 
                auther = User.objects.get(username=request.user.username),
                time = strftime("%Y %b %d %X",localtime()),
                post_id = check_pk,
                likes = 0,
             )   
            #url = reverse('story', kwargs={'story': check_pk})
            #return HttpResponseRedirect(url)
            #return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
            try:
                intopk = Post.objects.get(created_id=check_pk)
            except Story.DoesNotExist:
                intopk = Post.objects.order_by('-pk')[0]

            
            return HttpResponseRedirect("story",intopk.created_id)
            #story_list = Story.objects.filter(post_id=check_pk).all()
            #post_story = Post.objects.get(pk=check_pk)
            #return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})

        
        else:
            #return HttpResponseRedirect(request, 'mycontacts/show.html',{'story': story_list})   
            #url = reverse('story', kwargs={'story': check_pk})
            #return HttpResponseRedirect(url)
            story_list = Story.objects.filter(post_id=check_pk).all()
            post_story = Post.objects.get(created_id=check_pk)
            return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
    
    else:
        story_list = Story.objects.filter(post_id=check_pk).all()
        post_story = Post.objects.get(created_id=check_pk)
        
        if request.is_ajax():
            return render(request, 'storyteller_app/refresh_story.html',{'story': story_list, 'post': post_story})
        else:
            return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})
     
#message like   
def likes(request, pk):
    
    temp_pk = pk
    
    Story.objects.filter(pk=temp_pk).update(likes = F('likes')+1)
    intopk = Story.objects.get(pk=temp_pk)
    
    if request.is_ajax():
        story_list = Story.objects.filter(post_id=intopk.post_id).all()
        post_story = Post.objects.get(created_id=intopk.post_id)
        return render(request, 'storyteller_app/refresh_story.html',{'story': story_list, 'post': post_story})
    else:
        return redirect("story",intopk.post_id)

# collection_ehtml paginator
def collection_e(request):
    limit = 9
    contact_list = Post.objects.all().order_by('-pk')
    paginator = Paginator(contact_list, limit) # Show 25 contacts per page

    page = request.GET.get('page')
    
    try:
        contacts = paginator.page(page)    
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request, 'storyteller_app/refresh_post.html',{'contacts': contacts})
    else:
        return render(request, 'storyteller_app/collection_e.html', {'contacts': contacts})

# collection_f.html
def collection_f(request):
    
    return render(request,'storyteller_app/collection_f.html')
     
#create a new story
def addpost(request):
    
    post_list  = Post.objects.all()

    if request.method == 'POST':
        
        django_form = AddForm2(request.POST)
        if django_form.is_valid():
            new_title = django_form.data.get("new-title")
            first_sentence = django_form.data.get("first-sentence")
            
            Post.objects.create(
                storyTitle = new_title,
                created_id = int(round(time.time() * 1000)),
                created_at = strftime("%Y %b %d",localtime()),
                created_day = strftime("%d",localtime()),
                created_mon = strftime("%b",localtime()),
                post_likes = 0,
                firstSentence = first_sentence,
            )
            
            intopk = Post.objects.get(storyTitle=new_title)
            
            Story.objects.create(
                context =  first_sentence, 
                auther = User.objects.get(username=request.user.username),
                time = strftime("%Y %b %d %X",localtime()),
                post_id = intopk.created_id,
                likes = 0,
            )
            

            return redirect("story",intopk.created_id)
        
        else:
            post_list  = Post.objects.all()
            return render(request,'storyteller_app/collection_e.html',{'post': post_list})
    
    else:
        post_list  = Post.objects.all()
        return render(request,'storyteller_app/collection_e.html',{'post': post_list})

#index.html
def index(request):
    return render(request,'storyteller_app/index.html')
 
#story like
def post_likes(request, pk):
    
    temp_pk = pk
    Post.objects.filter(created_id=temp_pk).update(post_likes = F('post_likes')+1)
    contact_list = Post.objects.all().order_by('-pk')
    paginator = Paginator(contact_list, 9) # Show 25 contacts per page
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first pag.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    
    if request.is_ajax():
        return render(request, 'storyteller_app/refresh_post.html',{'contacts': contacts})
    else:
        return render(request, 'storyteller_app/collection_e.html', {'contacts': contacts})

#story like in chat room
def in_post_likes(request, pk):
    
    temp_pk = pk
    
    Post.objects.filter(created_id=temp_pk).update(post_likes = F('post_likes')+1)
    
    #return redirect("story",intopk.post_id)
    story_list = Story.objects.filter(post_id=temp_pk).all()
    post_story = Post.objects.get(created_id=temp_pk)
    
    if request.is_ajax():
       
        return render(request, 'storyteller_app/refresh_bottom.html',{'story': story_list, 'post': post_story})
    
    else:
    
        return render(request, 'storyteller_app/story.html',{'story': story_list, 'post': post_story})

#hot sort
def hot_sort(request):
    
    limit = 9
    contact_list = Post.objects.all().order_by('-post_likes')
    paginator = Paginator(contact_list, limit) # Show 25 contacts per page

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

#new sort
def new_sort(request):

    limit = 9
    contact_list = Post.objects.all().order_by('-pk')
    paginator = Paginator(contact_list, limit) # Show 25 contacts per page

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
    
@login_required
def personal(request):
    return render(request,'storyteller_app/personal.html')
    
    
def login(request):
    return render_to_response('registration/login.html',)      


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form })
 
    return render_to_response('registration/register.html', variables,)
 
def register_success(request):
    return render_to_response('registration/success.html',)
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')