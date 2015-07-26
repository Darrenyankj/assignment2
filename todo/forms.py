from todo.models import Todo
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button

class TodoForm(forms.ModelForm):
    class Meta: 
        model = Todo
        
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
    helper.add_input(Button('Delete', 'Delete', css_class='btn-primary', onclick='window.location.href="{}"'.format('delete')))