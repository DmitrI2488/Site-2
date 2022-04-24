from django.forms import ModelForm
from django import forms
from Home.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'rate')
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш коментарий'}),
            'rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваша оценка'}),
        }
