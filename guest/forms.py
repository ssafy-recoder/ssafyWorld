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
            }
        )
    )
    class Meta:
        model = Guest
        fields = ('content',)