from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Todo

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
    responsetext += "<p>" + "Do by: " + str(todo.todo_date) + "</p>"
    return HttpResponse(responsetext)