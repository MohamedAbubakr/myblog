from .models import Comment
from django.forms import ModelForm, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', ]
        widgets = {
            'comment_text': Textarea(attrs={'cols': 30, 'rows': 1}),}
