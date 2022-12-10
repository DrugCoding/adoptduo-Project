from .models import Stories, StoryComment, Image
from django import forms


class StoriesForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields = ["title", "content"]
        labels = {
            "title": "🗒️제목",
            "content": "📝내용",
            "image": "📸사진",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "게시글 제목을 입력해주세요.",
                }),

            "content": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "게시글을 입력해주세요.",
                }),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            "image",
        ]



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
