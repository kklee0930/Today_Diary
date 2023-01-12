from django import forms
from django.forms import ModelForm
from .models import DiaryArticle, Comments
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
        
class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = [
            # 'author',
            'comment',
            # 'likes',
            # 'comment_created_date',
            # 'comment_updated_date'
        ]
        labels = {
            # 'author': '👤작성자',
            'comment': '댓글로 공감해주세요',
            # 'likes': '👍좋아요',
            # 'comment_created_date': '📆작성일',
            # 'comment_updated_date': '수정일',
        }
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    # 'class': 'p-2',
                    'placeholder': '매너 댓글 부탁드려요😊 (댓글은 최대 150자까지 작성이 가능해요)',
                }
            ),
        }