from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
