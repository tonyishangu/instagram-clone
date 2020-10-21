from django import forms
from .models import Image,Comment,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewImagePost(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','user_profile','likes']
       
class UpdateProfile(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio','profile_pic']
		exclude = ['user']


class CreateComment(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']
		exclude = ['image','profile']