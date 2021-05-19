from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control'
                }
            )
    )
    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'type': 'password'
                }
            )
    )

class CustomUserCreationForm(UserCreationForm):
    choice_loc = [('1', '광주'), ('2', '경기'), ('3', '서울')]
    profile_img = forms.ImageField(
        label='프로필 사진',
        required=False,
    )
    username = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름을 입력하세요',
            }
        )
    )
    group = forms.CharField(
        label = '반',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '반을 입력하세요',
            }
        )
    )
    residence = forms.CharField(
        label='거주지역: ',
        widget=forms.Select(
            attrs={
                'name': 'located',
                'style': "width:100%",
            },
            choices=choice_loc
        )
    )
    like_language = forms.CharField(
        label = '선호하는 언어',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ex) C, C++, C#, Java, Python',
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 입력하세요',
                'type': 'password',
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호를 입력하세요',
                'type': 'password',
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('group','like_language', 'profile_img')