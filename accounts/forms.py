from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "name",
            "username",
            "email",
            "birthdate",
            'password1',
            'password2',
        )
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '실명을 입력해주세요!'
                }
            ),
            "username": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '추후 변경이 불가능해요!'
                }
            ),
            "email": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '예: user@email.com'
                }
            ),
            "birthdate": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '예: YYYY-MM-DD'
                }
            ),
            
        }
        labels = {
            "name": "📛이름",
            "username": "🆔아이디",
            "email": "📧이메일",
            "birthdate": "🎂생년월일", 
            "password1": "비밀번호",
            "password2": "비밀번호확인",
        }

