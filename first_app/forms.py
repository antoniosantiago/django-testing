from django import forms
from first_app.models import RegisterModel
from django.contrib.auth.models import User

class RegisterModelForm(forms.ModelForm):
    class Meta():
        model = RegisterModel
        fields = '__all__'

class UserModelForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
