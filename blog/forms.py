from .models import Comment, Audio
from django.forms import ModelForm, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', ]
        widgets = {
            'comment_text': Textarea(attrs={'cols': 30, 'rows': 1,
                                            'placeholder': 'Write a comment...',
                                            'class': 'form-control'}), }


class AudioForm(ModelForm):
    class Meta:
        model = Audio
        fields = ['name', 'url']
