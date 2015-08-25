import json

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Todo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from todo.forms import TodoForm
from django.conf.urls import url
from django.db.models import Q
from .models import Todo, Folder, Tag
from .forms import TodoForm, FolderForm, TagForm, TodoFormUpdate
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.serializers.json import DjangoJSONEncoder
from accounts.models import UserProfile

# Create your views here.

    
class TodoList(ListView): 
    model = Todo
    queryset = Todo.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        #self.request.user will contain the "User" object, however,
        #user field in the Todo model is an instance of "UserProfile" object
        #So need to ensure that when we filter all the user owned todos, we
        #filter using the 'correct' UserProfile instance based on logged in "User" object 
        #in self.request.user
        curruser = UserProfile.objects.get(user=self.request.user)
        folder = self.kwargs['folder']
        if folder == '':
            #filter based on current logged in user
            self.queryset = Todo.objects.filter(user=curruser)
            return self.queryset
        else:
            #filter based on current logged in user
            self.queryset = Todo.objects.all().filter(user=curruser).filter(folder__title__iexact=folder)
            return self.queryset
    
    def get_context_data(self, **kwargs):
        context = super(TodoList, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        #provided so that the avatar can be displayed in base.html
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


class TodoDetail(DetailView):
    model = Todo
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoDetail, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(TodoDetail, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoFormUpdate
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(TodoUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
    
class TodoByTag(ListView):
    model = Todo
    
    queryset = Todo.objects.all()
    def get_queryset(self):
        tags = self.kwargs['tags']
        pieces = tags.split('/') #extract different tags separated by /
        
        queries = [Q(tag__title__iexact=value) for value in pieces]
        # Take one Q object from the list
        query = queries.pop()
        # Or the Q object with the ones remaining in the list
        for item in queries:
            query |= item
        # Query the model
        curruser = UserProfile.objects.filter(user=self.request.user) #only query todos by curruser
        alltodos = Todo.objects.filter(user=curruser).filter(query).distinct().order_by('tag__title')
        self.queryset = alltodos #Setting the queryset to allow get_context_data to apply count
        return alltodos
    
    def get_context_data(self, **kwargs):
        context = super(TodoByTag, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


class MyView(TemplateView):
    folder_form_class = FolderForm
    tag_form_class = TagForm
    todo_form_class = TodoForm
    template_name = "todo/todo_hybrid.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        kwargs.setdefault("createfolder_form", self.folder_form_class())
        kwargs.setdefault("createtag_form", self.tag_form_class())
        kwargs.setdefault("createtodo_form", self.todo_form_class())
        #Added curruser so that profile picture of curruser can be rendered.
        kwargs.setdefault('curruser', UserProfile.objects.get(user=self.request.user))
        return super(MyView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
        }
        
        if "btn_createfolder" in request.POST['form']:
            form = self.folder_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                   createfolder_form=form)
            else:
                form.save()
                data = Folder.objects.all()
                result_list = list(data.values('id','title'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder))
        elif "btn_createtag" in request.POST['form']:
            form = self.tag_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                   createtag_form=form)
            else:
                form.save() #save the new object
                data = Tag.objects.all() # retrieve all records
                result_list = list(data.values('id','title'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
        elif "btn_createtodo" in request.POST['form']:
            form = self.todo_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                   createtodo_form=form) 
            else:
                try:
                    #Find out which user is logged in and get the correct UserProfile record.
                    curruser = UserProfile.objects.get(user=self.request.user)
                    obj = form.save(commit=False)
                    obj.user = curruser #Save the todo todo under that user
                    obj.save() #save the new object
                    
                except Exception, e:
                    print("errors" + str(e))
                response = {'status': 1, 'message':'ok'}
                return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
            
        return super(MyView, self).get(request)
    

class TodoDelete(DeleteView):
    model = Todo
    success_url = '/list/'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TodoDelete, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(TodoDelete, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
