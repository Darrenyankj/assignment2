from django.contrib import admin
from .models import Todo, Folder, Tag
# Register your models here.

class TodoInline(admin.StackedInline): #Demo StackedInline vs TabularInline
    model = Todo
    fields = ('title',) 
    extra = 0
    
class FolderAdmin(admin.ModelAdmin):
    inlines = [TodoInline,]
    
    model = Folder


#http://stackoverflow.com/questions/6479999/django-admin-manytomany-inline-has-no-foreignkey-to-error    
#https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models
class TaggedTodoInline(admin.TabularInline): 
    model = Todo.tag.through
    extra = 0
    
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedTodoInline,]
    model = Tag

admin.site.register(Todo)
admin.site.register(Tag, TagAdmin)
admin.site.register(Folder, FolderAdmin)