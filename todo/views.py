from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Todo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from todo.forms import TodoForm
from django.conf.urls import url
from django.db.models import Q


# Create your views here.
def todo_list(request):
    alltodo = Todo.objects.all()
    return render(request, 'todo/index.html', {'things': alltodo}) 

'''def todo_list(request):
    alltodo = Todo.objects.all()
    responsetext = ""
    for todo in alltodo:
        url = reverse('things_detail', args=str(todo.id))
        responsetext += "<a href='"+ url + "'>"
        responsetext += "<h2>" + todo.title + "</h2></a>"
    return HttpResponse(responsetext)'''

    
def todo_detail(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    responsetext = ""
    responsetext += "<h2>" + todo.title + "</h2>"
    responsetext += "<p>" + todo.content + "</p>"
    responsetext += "<p>" + "Do by: " + str(todo.due) + "</p>"
    return HttpResponse(responsetext)
    
class TodoList(ListView):
    #https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-display/
    model = Todo
    
    def get_queryset(self):
        folder = self.kwargs['folder']
        if folder == '':
            self.queryset = Todo.objects.all()
            return self.queryset
        else:
            self.queryset = Todo.objects.filter(folder__title__iexact=folder)
            return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(TodoList, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        return context
            
class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm

class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    
class TodoDetail(DetailView):
    model = Todo
    
class TodoDelete(DeleteView):
    model = Todo
    
    success_url = url(r'^listall/$', ListView.as_view(model=Todo), name='todo_listall')
    
class TodobyTag(ListView):
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
        alltodo = Todo.objects.filter(query).distinct().order_by('tag__title')
        self.queryset = alltodo #Setting the queryset to allow get_context_data to apply count
        return alltodo
    
    def get_context_data(self, **kwargs):
        context = super(TodobyTag, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        return context