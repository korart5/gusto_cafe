from django import forms
from .models import Message

class FormMessange(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Имя', 'required': 'required'}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'class': 'form-control',
                                                              'placeholder': 'Email', 'required': 'required'}))
    user_messange = forms.CharField(max_length=400,
                                widget=forms.Textarea(attrs={'type': 'messange', 'id': 'messange', 'class': 'form-control',
                                                             'rows': '4', 'placeholder': 'Messange', 'required': 'required'}))

    class Meta():
        model = Message
        fields = {'user_name', 'user_email', 'user_messange'}

class FormAdd(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Имя', 'required': 'required'}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'class': 'form-control',
                                                              'placeholder': 'Email', 'required': 'required'}))
    user_messange = forms.CharField(max_length=400,
                                widget=forms.Textarea(attrs={'type': 'messange', 'id': 'messange', 'class': 'form-control',
                                                             'rows': '4', 'placeholder': 'Messange', 'required': 'required'}))

    class Meta():
        model = Message
        fields = {'user_name', 'user_email', 'user_messange'}

class FormDelete(forms.ModelForm):
    user_name = forms.CharField(max_length=40,
                                widget=forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                                              'placeholder': 'Имя', 'required': 'required'}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'email', 'class': 'form-control',
                                                              'placeholder': 'Email', 'required': 'required'}))
    user_messange = forms.CharField(max_length=400,
                                widget=forms.Textarea(attrs={'type': 'messange', 'id': 'messange', 'class': 'form-control',
                                                             'rows': '4', 'placeholder': 'Messange', 'required': 'required'}))

    class Meta():
        model = Message
        fields = {'user_name', 'user_email', 'user_messange'}