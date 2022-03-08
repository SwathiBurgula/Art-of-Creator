from django.forms import ModelForm, widgets
from django import forms
from .models import Post, Preference

class ProjectForm(ModelForm):
    class Meta:
        model =  Post
        # fields = '__all__'
        fields = ['name','image','Categeory','View','Likes','Shares']
        widgets ={
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for label,field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})

        # self.fields['name'].widget.attrs.update({'class':'input','placeholder':'Enter project name'})



class ReviewForm(ModelForm):
    class Meta:
        model = Preference
        fields=['value','date']
        labels={
            'date': 'date',
            'value':'like'
        }
        


    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for label,field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})