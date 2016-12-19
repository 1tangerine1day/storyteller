{"filter":false,"title":"views.py","tooltip":"/storyteller_app/views.py","undoManager":{"mark":80,"position":80,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":118,"column":50},"action":"insert","lines":["from django.shortcuts import render","from django.shortcuts import render_to_response","from django.shortcuts import redirect","from django.core.urlresolvers import reverse","# Create your views here.","from .forms import AddForm, AddForm2","from .models import Story, Post","from django.http import HttpResponseRedirect","from time import localtime,strftime","from django.db.models import F","","        ","        ","def show(request, pk):","    ","    check_pk = pk","    ","    if request.method == 'POST':","        ","        django_form = AddForm(request.POST)","        if django_form.is_valid():","            new_context = django_form.data.get(\"context\")","            ","            Story.objects.create(","                context =  new_context, ","                auther = \"auther\",","                time = strftime(\"%Y %b %d %X\",localtime()),","                post_id = check_pk,","                likes = 0,","                )","                ","            ","            ","            #url = reverse('story', kwargs={'story': check_pk})","            #return HttpResponseRedirect(url)","            story_list = Story.objects.filter(post_id=check_pk).all()","            post_story = Post.objects.get(pk=check_pk)","            return render(request, 'mycontacts/show.html',{'story': story_list, 'post': post_story})","            ","        ","        else:","            #return HttpResponseRedirect(request, 'mycontacts/show.html',{'story': story_list})   ","            #url = reverse('story', kwargs={'story': check_pk})","            #return HttpResponseRedirect(url)","            story_list = Story.objects.filter(post_id=check_pk).all()","            post_story = Post.objects.get(pk=check_pk)","            return render(request, 'mycontacts/show.html',{'story': story_list, 'post': post_story})","    ","    else:","        story_list = Story.objects.filter(post_id=check_pk).all()","        post_story = Post.objects.get(pk=check_pk)","        return render(request, 'mycontacts/show.html',{'story': story_list, 'post': post_story})"," ","        ","def likes(request, pk):","    ","    temp_pk = pk","    ","    Story.objects.filter(pk=temp_pk).update(likes = F('likes')+1)","    intopk = Story.objects.get(pk=temp_pk)","    ","    #story_list = Story.objects.filter(post_id=1234).all()","    #return HttpResponseRedirect(\"url 'story' temp_pk\")","    #return render_to_response('mycontacts/show.html',{'story': story_list})","    #url = reverse('story', kwargs={'story': temp_pk})","    #return HttpResponseRedirect(url)","    ","    return redirect(\"story\",intopk.post_id)","    ","def collection_e(request):","    post_list = Post.objects.all()","    return render(request,'mycontacts/collection_e.html',{","        'post_list': post_list,","    })","    ","    ","def collection_f(request):","    return render(request,'mycontacts/collection_f.html')","    ","    ","def addpost(request):","","    if request.method == 'POST':","        ","        django_form = AddForm2(request.POST)","        if django_form.is_valid():","            new_title = django_form.data.get(\"new-title\")","            first_sentence = django_form.data.get(\"first-sentence\")","            ","            Post.objects.create(","                storyTitle = new_title,","                created_at = strftime(\"%Y %b %d\",localtime()),","                firstSentence = first_sentence,","            )","            ","            intopk = Post.objects.get(storyTitle=new_title)","            ","            Story.objects.create(","                context =  first_sentence, ","                auther = \"auther\",","                time = strftime(\"%Y %b %d %X\",localtime()),","                post_id = intopk.pk,","                likes = 0,","                )","            ","","        ","            post_list = Post.objects.all()","            return redirect(\"story\",intopk.pk)","        else:","            #return HttpResponseRedirect(request, 'mycontacts/show.html',{'story': story_list})   ","            return HttpResponseRedirect(\"/\")","    else:","        post_list = Post.objects.all()","        return render(request,'mycontacts/collection_e.html',{'post': post_list})","","","def index(request):","    return render(request,'mycontacts/index.html')"]}],[{"start":{"row":114,"column":31},"end":{"row":114,"column":41},"action":"remove","lines":["mycontacts"],"id":3}],[{"start":{"row":114,"column":31},"end":{"row":114,"column":32},"action":"insert","lines":["s"],"id":4}],[{"start":{"row":114,"column":32},"end":{"row":114,"column":33},"action":"insert","lines":["t"],"id":5}],[{"start":{"row":114,"column":33},"end":{"row":114,"column":34},"action":"insert","lines":["o"],"id":6}],[{"start":{"row":114,"column":34},"end":{"row":114,"column":35},"action":"insert","lines":["r"],"id":7}],[{"start":{"row":114,"column":35},"end":{"row":114,"column":36},"action":"insert","lines":["y"],"id":8}],[{"start":{"row":114,"column":36},"end":{"row":114,"column":37},"action":"insert","lines":["t"],"id":9}],[{"start":{"row":114,"column":37},"end":{"row":114,"column":38},"action":"insert","lines":["e"],"id":10}],[{"start":{"row":114,"column":38},"end":{"row":114,"column":39},"action":"insert","lines":["l"],"id":11}],[{"start":{"row":114,"column":39},"end":{"row":114,"column":40},"action":"insert","lines":["l"],"id":12}],[{"start":{"row":114,"column":40},"end":{"row":114,"column":41},"action":"insert","lines":["e"],"id":13}],[{"start":{"row":114,"column":41},"end":{"row":114,"column":42},"action":"insert","lines":["r"],"id":14}],[{"start":{"row":114,"column":42},"end":{"row":114,"column":43},"action":"insert","lines":["_"],"id":15}],[{"start":{"row":114,"column":43},"end":{"row":114,"column":44},"action":"insert","lines":["a"],"id":16}],[{"start":{"row":114,"column":44},"end":{"row":114,"column":45},"action":"insert","lines":["p"],"id":17}],[{"start":{"row":114,"column":45},"end":{"row":114,"column":46},"action":"insert","lines":["p"],"id":18}],[{"start":{"row":118,"column":27},"end":{"row":118,"column":37},"action":"remove","lines":["mycontacts"],"id":19},{"start":{"row":118,"column":27},"end":{"row":118,"column":42},"action":"insert","lines":["storyteller_app"]}],[{"start":{"row":77,"column":27},"end":{"row":77,"column":37},"action":"remove","lines":["mycontacts"],"id":20},{"start":{"row":77,"column":27},"end":{"row":77,"column":42},"action":"insert","lines":["storyteller_app"]}],[{"start":{"row":71,"column":27},"end":{"row":71,"column":37},"action":"remove","lines":["mycontacts"],"id":21},{"start":{"row":71,"column":27},"end":{"row":71,"column":42},"action":"insert","lines":["storyteller_app"]}],[{"start":{"row":37,"column":36},"end":{"row":37,"column":46},"action":"remove","lines":["mycontacts"],"id":22},{"start":{"row":37,"column":36},"end":{"row":37,"column":51},"action":"insert","lines":["storyteller_app"]}],[{"start":{"row":46,"column":36},"end":{"row":46,"column":46},"action":"remove","lines":["mycontacts"],"id":23},{"start":{"row":46,"column":36},"end":{"row":46,"column":51},"action":"insert","lines":["storyteller_app"]}],[{"start":{"row":51,"column":32},"end":{"row":51,"column":42},"action":"remove","lines":["mycontacts"],"id":24},{"start":{"row":51,"column":32},"end":{"row":51,"column":47},"action":"insert","lines":["storyteller_app"]}],[{"start":{"row":91,"column":62},"end":{"row":92,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":92,"column":0},"end":{"row":92,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":92,"column":16},"end":{"row":92,"column":27},"action":"insert","lines":["created_day"],"id":26}],[{"start":{"row":92,"column":27},"end":{"row":92,"column":28},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":92,"column":28},"end":{"row":92,"column":29},"action":"insert","lines":["="],"id":28}],[{"start":{"row":92,"column":29},"end":{"row":92,"column":30},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":92,"column":30},"end":{"row":92,"column":63},"action":"insert","lines":["strftime(\"%Y %b %d\",localtime()),"],"id":30}],[{"start":{"row":92,"column":40},"end":{"row":92,"column":45},"action":"remove","lines":["%Y %b"],"id":31}],[{"start":{"row":92,"column":40},"end":{"row":92,"column":41},"action":"remove","lines":[" "],"id":32}],[{"start":{"row":92,"column":57},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":93,"column":0},"end":{"row":93,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":93,"column":16},"end":{"row":93,"column":57},"action":"insert","lines":["created_day = strftime(\"%d\",localtime()),"],"id":34}],[{"start":{"row":93,"column":26},"end":{"row":93,"column":27},"action":"remove","lines":["y"],"id":35}],[{"start":{"row":93,"column":25},"end":{"row":93,"column":26},"action":"remove","lines":["a"],"id":36}],[{"start":{"row":93,"column":24},"end":{"row":93,"column":25},"action":"remove","lines":["d"],"id":37}],[{"start":{"row":93,"column":24},"end":{"row":93,"column":25},"action":"insert","lines":["m"],"id":38}],[{"start":{"row":93,"column":25},"end":{"row":93,"column":26},"action":"insert","lines":["o"],"id":39}],[{"start":{"row":93,"column":26},"end":{"row":93,"column":27},"action":"insert","lines":["n"],"id":40}],[{"start":{"row":93,"column":41},"end":{"row":93,"column":42},"action":"remove","lines":["d"],"id":41}],[{"start":{"row":93,"column":41},"end":{"row":93,"column":42},"action":"insert","lines":["b"],"id":42}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "],"id":43}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":44}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":45}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":22},"action":"insert","lines":["def show(request, pk):"],"id":46}],[{"start":{"row":12,"column":22},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":54},"action":"insert","lines":["return render(request, 'storyteller_app/show.html'"],"id":48}],[{"start":{"row":13,"column":54},"end":{"row":13,"column":55},"action":"insert","lines":[")"],"id":49}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["show"],"id":50},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["e"],"id":51}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"remove","lines":["e"],"id":52}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["r"],"id":53}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["s"],"id":54}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["t"],"id":55}],[{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"insert","lines":["o"],"id":56}],[{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"insert","lines":["r"],"id":57}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["y"],"id":58}],[{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["_"],"id":59}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["p"],"id":60}],[{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["a"],"id":61}],[{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["g"],"id":62}],[{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["e"],"id":63}],[{"start":{"row":13,"column":44},"end":{"row":13,"column":48},"action":"remove","lines":["show"],"id":64},{"start":{"row":13,"column":44},"end":{"row":13,"column":45},"action":"insert","lines":["s"]}],[{"start":{"row":13,"column":45},"end":{"row":13,"column":46},"action":"insert","lines":["t"],"id":65}],[{"start":{"row":13,"column":46},"end":{"row":13,"column":47},"action":"insert","lines":["o"],"id":66}],[{"start":{"row":13,"column":47},"end":{"row":13,"column":48},"action":"insert","lines":["r"],"id":67}],[{"start":{"row":13,"column":48},"end":{"row":13,"column":49},"action":"insert","lines":["y"],"id":68}],[{"start":{"row":12,"column":25},"end":{"row":12,"column":26},"action":"remove","lines":["k"],"id":69}],[{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":["p"],"id":70}],[{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":[" "],"id":71}],[{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":[","],"id":72}],[{"start":{"row":12,"column":0},"end":{"row":13,"column":56},"action":"remove","lines":["def story_page(request):","    return render(request, 'storyteller_app/story.html')"],"id":73}],[{"start":{"row":121,"column":55},"end":{"row":122,"column":0},"action":"insert","lines":["",""],"id":74},{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":122,"column":4},"end":{"row":123,"column":0},"action":"insert","lines":["",""],"id":75},{"start":{"row":123,"column":0},"end":{"row":123,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":123,"column":0},"end":{"row":123,"column":4},"action":"remove","lines":["    "],"id":76}],[{"start":{"row":123,"column":0},"end":{"row":124,"column":56},"action":"insert","lines":["def story_page(request):","    return render(request, 'storyteller_app/story.html')"],"id":77}],[{"start":{"row":121,"column":26},"end":{"row":121,"column":27},"action":"insert","lines":[" "],"id":78}],[{"start":{"row":123,"column":0},"end":{"row":124,"column":56},"action":"remove","lines":["def story_page(request):","    return render(request, 'storyteller_app/story.html')"],"id":79}],[{"start":{"row":122,"column":4},"end":{"row":123,"column":0},"action":"remove","lines":["",""],"id":80}],[{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"remove","lines":["    "],"id":81}],[{"start":{"row":121,"column":56},"end":{"row":122,"column":0},"action":"remove","lines":["",""],"id":82}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":3,"column":44},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1482080102535,"hash":"05265f9dae422052373f432b8525f5747dc77407"}