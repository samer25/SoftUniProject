from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from user.models import ProfileUser


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        for field_name in ['username', 'password1', 'password2', 'email']:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class ProfileUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ProfileUser
        exclude = ['user']


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
