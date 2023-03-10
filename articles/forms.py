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
            'title': 'βοΈμ λͺ©',
            'content': 'πλ΄μ©',
            'hashtag': 'π·οΈνκ·Έ',
            'image': 'π·μΈλ€μΌμ¬μ§',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'μ λͺ©μ μλ ₯νμΈμ!'
                }
            ),
            'content': SummernoteWidget(
                attrs={
                    'placeholder': 'λ΄μ©μ μλ ₯νμΈμ!',
                    'summernote': {
                        'width': '100%',
                        'height': '380px',
                    }
                }
            ),
            'hashtag': forms.TextInput(
                attrs={
                    'placeholder': '#ν΄μνκ·Έλ₯Ό μλ ₯νμΈμ!'
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
            # 'author': 'π€μμ±μ',
            'comment': 'λκΈλ‘ κ³΅κ°ν΄μ£ΌμΈμ',
            # 'likes': 'πμ’μμ',
            # 'comment_created_date': 'πμμ±μΌ',
            # 'comment_updated_date': 'μμ μΌ',
        }
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    # 'class': 'p-2',
                    'placeholder': 'λ§€λ λκΈ λΆνλλ €μπ (λκΈμ μ΅λ 150μκΉμ§ μμ±μ΄ κ°λ₯ν΄μ)',
                }
            ),
        }