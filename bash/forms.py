from django.forms import ModelForm, TextInput, EmailInput, Textarea, Select
from users.models import Profiles, Message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profiles
#         fields = ["user", "name","email","username","level","stars","bio","description"]
      

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["subject","message"]
        widgets = {
            'subject': TextInput(attrs={
                'class': "form__subject",
                'placeholder': 'What do you want to wish them for?'
                }),
            'message': Textarea(attrs={
                'class': "form__message", 
                'placeholder': 'Enter your message'
                }), 
           
        }
        
        

# class EditableProfileForm(ModelForm):
#     class Meta:
#         model = Profiles
#         fields = ["name","email","username","bio","description","profile_image","background_banner","location","github","linkedin",'website','youtube']
      
      