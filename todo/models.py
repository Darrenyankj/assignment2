from django.db import models
from django.core.urlresolvers import reverse

# Create your models here
class Todo(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField(blank=True) #not a required field
    due = models.DateTimeField(null=True, blank=True) #due datetime is optional
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    done = models.BooleanField(default=False)
    #folder is optional
    folder = models.ForeignKey('Folder', related_name= "things", null=True, blank=True)
    #tag is optional
    tag = models.ManyToManyField('Tag', related_name='things', null=True, blank=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})
        

class Folder(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
        
class Tag(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    