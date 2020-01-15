from django import forms
from django.forms import ModelForm
from .models import dr_register,usr_register
class doctor_r(ModelForm):
    class Meta:
        model = dr_register
        fields = ['firstname' , 'lastname' ,'username', 'email','date','password1','password2' ,'myfile']
        widgets = {
            'firstname':forms.TextInput(attrs = {
                'placeholder':'enter your firstname'
            }),
            'lastname':forms.TextInput(attrs = {
                'placeholder':'enter your lastname'
                }),
            'username':forms.TextInput(attrs = {
                'placeholder':'enter your username'
                }),
            'email':forms.TextInput(attrs = {
                'placeholder':'enter your lastname'
                }),
            'password1':forms.PasswordInput(attrs = {'placeholder':'type ur password'}),
            'password2':forms.PasswordInput(attrs = {'placeholder':'confirm ur password'}),
            'email':forms.EmailInput(attrs = {'placeholder':'type ur valid email'}),
            'date':forms.DateInput(attrs = {'placeholder':'enter ur date of birth'}),
        }
class usr_r(ModelForm):
    class Meta:
        model = usr_register
        fields = ['first_name' , 'last_name' ,'user_name', 'email','password1','password2' ,'myfile']
        widgets = {
            'first_name':forms.TextInput(attrs = {
                'placeholder':'enter your firstname'
            }),
            'last_name':forms.TextInput(attrs = {
                'placeholder':'enter your lastname'
                }),
            'user_name':forms.TextInput(attrs = {
                'placeholder':'enter your username'
                }),
            'email':forms.TextInput(attrs = {
                'placeholder':'enter your lastname'
                }),
            'password1':forms.PasswordInput(attrs = {'placeholder':'type ur password'}),
            'password2':forms.PasswordInput(attrs = {'placeholder':'confirm ur password'}),
            'email':forms.EmailInput(attrs = {'placeholder':'type ur valid email'}),
        }
class usr_login(ModelForm):
    class Meta:
        model = usr_register
        fields = ['user_name' ,'password1']
        widgets = {
            'user_name':forms.TextInput(attrs = {
                'placeholder':'enter your username'
                }),
            'password1':forms.PasswordInput(attrs = {'placeholder':'type ur password'}),
        }

class dr_login(ModelForm):
    class Meta:
        model = dr_register
        fields = ['username' ,'password1']
        widgets = {
            'username':forms.TextInput(attrs = {
                'placeholder':'enter your username'
                }),
            'password1':forms.PasswordInput(attrs = {'placeholder':'type ur password'}),
        }