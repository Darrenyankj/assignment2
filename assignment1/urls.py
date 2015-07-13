from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo import views

urlpatterns = patterns('',

    url(r'^todo/(?P<todo_id>\d+)$', views.todo_detail, name="detail"),
    url(r'^list/$', views.todo_list, name= "things_list"),
    url(r'^admin/', include(admin.site.urls)),
)

