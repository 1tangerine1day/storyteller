from django.contrib import admin
from .models import Story, Post, Follow, Img



class showimg(admin.ModelAdmin):
    list_display = ['username', 'img']
    class Meta:
        model = Img


class showpost(admin.ModelAdmin):
    list_display = ['storyTitle', 'created_id', 'created_at' ,'post_likes', 'firstSentence','created_auther']
    class Meta:
        model = Post
        
        
class showfollow(admin.ModelAdmin):
    list_display = ['follow_post', 'follow_who', 'follow_created_id',]
    class Meta:
        model = Follow
        
class showstory(admin.ModelAdmin):
    list_display = ['context', 'time', 'auther', 'post_id', 'story_id', 'likes','auther_img',]
    class Meta:
        model = Story
        
        
admin.site.register(Story,showstory)
admin.site.register(Post,showpost)
admin.site.register(Follow,showfollow)
admin.site.register(Img,showimg)
