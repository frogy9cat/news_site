from django import forms
from django.forms import Textarea, TextInput, ImageField, PasswordInput
from .models import Category1, News, Authorization

class News_form(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'photos', 'info', 'category1']
        widgets = {
            'title': TextInput(attrs={"class": "form-control"}),
            'info': Textarea(attrs={"class": "form-control"})
        }




class Auth_form(forms.ModelForm):
    class Meta:
        model = Authorization
        fields = ['name', 'login', 'password']
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'login': TextInput(attrs={'class':'form-control'}),
            'password': PasswordInput(attrs={'class':'form-control'})
        }


class Login_form(forms.ModelForm):
    class Meta:
        model = Authorization
        fields = ['login', 'password']
        widgets = {
            'login': TextInput(attrs={'class':'form-control'}),
            'password': TextInput(attrs={'class':'form-control'})
            }
            

# class AuthForm(forms.ModelForm):
#     class Meta:
#         model = Auth
#         fields = ['login', 'password']
#         widgets = {
#             'login': 
#         }