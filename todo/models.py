from django.db import models

# Create your models here
class Todo(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    todo_date = models.DateField()
    
    def __unicode__(self):
        return self.title
