from django.urls import path
from django.conf.urls import url

from posts.views import post_list, post_create, post_update, post_delete, post_detail

urlpatterns = [

    url(r'^$', post_list),
    url(r'create/$', post_create),
    url(r'(?P<id>.+[a-zA-Z*=\-0-9])/edit/$', post_update),
    url(r'(?P<id>.+[a-zA-Z*=\-0-9])/delete/$', post_delete),
    url(r'(?P<id>.+[a-zA-Z*=\-0-9])/$', post_detail),

]

