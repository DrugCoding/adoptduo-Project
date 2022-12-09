from .models import Stories, StoryComment
from django import forms

class StoriesForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields = ["title","name", "breed", "content", "image"]
        labels = {
            "title": "🗒️제목",
            "name": "✏반려동물 이름",
            "breed": "😺품종",
            "content": "📝내용",
            "image": "📸사진",
        }
        
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "게시글 제목을 입력해주세요.",
                }),
            "name": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "반려동물의 이름을 입력해주세요.",
                }),
            
            "breed": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "반려동물의 품종을 작성해주세요.",
                }),
            "content": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "게시글을 입력해주세요.",
                }),
            "image": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "사진을 입력해주세요.",
                }),
        }

class Stories_CommentForm(forms.ModelForm):
    class Meta:
        model = StoryComment
        fields = ["content",]
        labels = {
            "content": "댓글입력",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 1, "cols": 10}),
        }