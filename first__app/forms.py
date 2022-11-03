from django import forms
from .models import Comment, Tree


class TreeForm(forms.ModelForm):
  class Meta:
    model = Tree
    exclude = [

    ]
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "title",
            "content",
        ]
