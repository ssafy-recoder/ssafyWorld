from django import forms
from .models import Photo, Comment

class CommentForm(forms.ModelForm):
    label='댓글',
    widgets=forms.Textarea(
        attrs={
            'rows':3,
            'cols': 100,
            'width':'200px',
        }
    )

    class Meta:
        model = Comment
        fields = ('content',)