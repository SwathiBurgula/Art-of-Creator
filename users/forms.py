from email.message import Message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels ={
            'first_name': 'Name',
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for label,field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user','username','email']
    
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)

            for label,field in self.fields.items():
                field.widget.attrs.update({'class': 'input input--text', 'placeholder':'Enter value'})
