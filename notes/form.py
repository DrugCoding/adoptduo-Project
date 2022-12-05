from django import forms
from .models import Notes

class Notes(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ("title", "content")
        labels = {
            "title": "제목",
            "content": "내용",
        }

 