from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ClearableFileInput
from .models import Articles, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class ArticlesForm(ModelForm):
    full_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Articles
        fields = ['title', 'intro', 'full_text', 'date', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Обзор статьи'
            }),
            "date": DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "image": ClearableFileInput(attrs={
                'class': 'form-control-file',
                'type': 'file'
            })
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']