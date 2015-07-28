from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo import views
from todo.models import Todo
from django.views.generic import ListView, DetailView

urlpatterns = patterns('',

    #url(r'^todo/(?P<todo_id>\d+)$', views.todo_detail, name="detail"),
    url(r'^listall/$', ListView.as_view(model=Todo), name='todo_listall'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/(?P<folder>.*)$', views.TodoList.as_view(), name='todo_list'),
    url(r'^tag/(?P<tags>.*)$', views.TodobyTag.as_view(), name='todo_list'),
    #url(r'^detail/(?P<pk>\d+)$', DetailView.as_view(model=Todo), name='detail'),
    url(r'^add/$', views.TodoCreate.as_view(), name='todo_add'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.TodoUpdate.as_view(),  name='todo_update'),
    url(r'^todo/(?P<pk>\d+)$', views.TodoDetail.as_view(),  name='detail'),
    url(r'^todo/(?P<pk>\d+)/edit/delete/$', views.TodoDelete.as_view(),  name='todo_delete'),
)
