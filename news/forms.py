from django import forms
from .models import News,Cat

class CreateNews(forms.ModelForm):

    class Meta:
        model = News
        fields = (
            'nc',
            'title',
            'image',
            'content',
        )