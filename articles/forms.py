from django import forms
from django.forms import ModelForm
from .models import DiaryArticle
from django_summernote.widgets import SummernoteWidget

class DiaryForm(ModelForm):
    class Meta:
        model = DiaryArticle
        fields = [
            'title',
            'content',
            'hashtag',
            'image',
        ]
        labels = {
            'title': '✍️제목',
            'content': '📝내용',
            'hashtag': '🏷️태그',
            'image': '📷썸네일사진',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': '제목을 입력하세요!'
                }
            ),
            'content': SummernoteWidget(
                attrs={
                    'placeholder': '내용을 입력하세요!',
                    'summernote': {
                        'width': '100%',
                        'height': '380px',
                    }
                }
            ),
            'hashtag': forms.TextInput(
                attrs={
                    'placeholder': '#해시태그를 입력하세요!'
                }
            ),
        }