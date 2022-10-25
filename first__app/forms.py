from django import forms
from django import forms
from .models import People, Comment


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = [
          "user",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "title",
            "content",
        ]
