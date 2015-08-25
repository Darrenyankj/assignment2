from django import forms
from .models import Todo, Folder, Tag
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Button, HTML, Div, Field, Row, Fieldset


class TodoForm(forms.ModelForm):
    class Meta: 
        model = Todo
        fields = '__all__'
        
    
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "todoform"
        
        #Create a new folder select list, with added css and style codes
        folder = Div('folder', css_class="col-xs-12", style="padding:0px;") 
        self.helper.layout.pop(6) #remove the original folder select list 
        #Insert new folder select list with a "Create New Folder" button as a Fieldset
        self.helper.layout.insert(6,Fieldset("Select folder",folder, Button("createfoldermodal", value="Create New Folder", css_class="btn btn-primary btn-sm col-xs-12 ", data_toggle="modal", data_target="#myModal")))
        
        #Create a new tag multi-select list, with added css and style codes
        tag = Div('tag',css_class = "col-xs-12", style="padding:0px;") 
        #oldtagselect = self.helper.layout.pop(7) #remove the original tag multi-select list
        #Insert new tag multi-select list with a "Create New Tag" button as a Fieldset
        self.helper.layout.insert(7, Fieldset("Select Tag",tag, Button("createtagmodal", value="Create New Tag", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal2")))
        
        #Create a "Create New Note" button 
        self.helper.layout.append(Button('btn_createtodo', 'Create Todo', css_class='createtodo', style="margin-top:15px;"))
        #Add a hidden field 'btn_createnote' so that it will be submitted together in the form to allow server side to 'know'
        #that this button has been clicked
        self.helper.layout.append(Hidden(name='btn_createtodo', value="btn_createtodo"))
        
        
        
    def full_clean(self):
        #http://stackoverflow.com/questions/4340287/override-data-validation-on-one-django-form-element
        super(TodoForm, self).full_clean()
        if 'tag' in self._errors:
            self.cleaned_data['tag'] = []
            print("remove tag errors")
            del self._errors['tag']
            
class TodoFormUpdate(forms.ModelForm):
    class Meta: 
        model = Todo
        #fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(TodoFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "todoformupdate"
        
        self.helper.add_input(Submit('submit', 'Update'))
            
class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "folderform"
        self.helper.layout.append(Hidden(name='btn_createfolder', value="btn_createfolder"))
        self.helper.layout.append(Button('btn_createfolder', 'Create Folder', css_class='createfolder', data_dismiss="modal"))
        

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "tagform"
        self.helper.layout.append(Hidden(name='btn_createtag', value="btn_createtag"))
        self.helper.layout.append(Button('btn_createtag', 'Create Tag', css_class='createtag', data_dismiss="modal"))

