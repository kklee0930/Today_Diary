from django import forms
from django.forms import ModelForm
from .models import DiaryArticle

class DiaryForm(ModelForm):
    class Meta:
        model = DiaryArticle
        fields = [
            'title',
            'content',
            'hashtag',
        ]
        labels = {
            'title': '✍️제목',
            'content': '📝내용',
            'hashtag': '🏷️태그',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목을 입력하세요!'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'placeholder': '내용을 입력하세요!'
                }
            ),
            'hashtag': forms.TextInput(
                attrs={
                    'placeholder': '#해시태그를 입력하세요!'
                }
            ),
        }