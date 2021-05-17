from django import forms
from .models import HomeComment

class HomeCommentForm(forms.ModelForm):

    class Meta:
        model = HomeComment
        fields = ('content',)