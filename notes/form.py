from django import forms
from .models import Notes

class  NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ("title", "content")
        labels = {
            "title": "🗒️제목",
            "content": "🖋️쪽지 내용",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "제목을 입력해주세요.",
                }),
            "content": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "쪽지를 작성해주세요.",
                }),}

 