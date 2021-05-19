from django import forms
from django.db import models
from .models import Guest

class guestForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용 입력하세요',
                'cols': '45',
                'rows': '6',
                'style': 'border-radius: 10px; resize:none;',
            }
        )
    )
    class Meta:
        model = Guest
        fields = ('content',)