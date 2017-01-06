"""storyteller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from storyteller_app import views
from django.contrib.auth.views import login
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^story/(?P<pk>\d+)/', views.story, name='story'),
    url(r'^likes/(?P<pk>\d+)/', views.likes, name='likes'),
    url(r'^post_likes/(?P<pk>\d+)/', views.post_likes, name='post_likes'),
    url(r'^in_post_likes/(?P<pk>\d+)/', views.in_post_likes, name='in_post_likes'),
    url(r'^follow/(?P<pk>\d+)/', views.follow, name='follow'),
    url(r'^finish/', views.collection_f, name='collection_f'),
    url(r'^post/', views.addpost, name = 'addpost'),
    url(r'^hot/', views.hot_sort, name = 'hot_sort'),
    url(r'^new/', views.new_sort, name = 'new_sort'),
    url(r'^$', views.index, name='index'),
    url(r'^editing/', views.collection_e, name='collection_e'),
    url(r'^personal/(?P<pk>\w+)', views.personal, name='personal'),
    url(r'^login/$', login),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', views.logout_page),
    url(r'^upload_img/$', views.upload_img, name="upload_img"),
    
    url(r'^index/', views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

