from django.forms import ModelForm
from django import forms
from .models import feedback


class FeedBack(ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'theme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше сообщение'}),
        }


class review(ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше сообщение'}),
        }
