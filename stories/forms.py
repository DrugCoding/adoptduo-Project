from .models import Stories, StoryComment
from django import forms

class StoriesForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields = ["title", "content", "image"]
        label = {
            "title": "제목",
            "content": "내용",
            "image": "사진",
        }

class Stories_CommentForm(forms.ModelForm):
    class Meta:
        model = StoryComment
        fields = ["content"]
        label = {
            "content": "댓글입력",
        }