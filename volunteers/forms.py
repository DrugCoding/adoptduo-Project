from django import forms
from .models import Volunteer, VolunteerComment
from django_summernote.widgets import SummernoteWidget
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'title',
            'area',
            'adopt_location',
            'adopt_date',
            'content',
        ]
        labels = {
            'title': '제목',
            'area': '출발지역',
            'adopt_location': '도착지역',
            'adopt_date': '이동날짜',
            'content': '추가내용',
        }
        widgets = {
            'area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '출발하는 지역'
                }
            ),
            'adopt_location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '도착하는 지역'
                }
            ),
            'adopt_date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'yyyy-mm-dd'
                }
            ),
            'content': SummernoteWidget(),
        }

class VolunteerCommentForm(forms.ModelForm):
    class Meta:
        model = VolunteerComment
        fields = ['content',]
        # labels = {
        #     "content": "댓글입력",
        # }
        # widgets = {
        #     "content": forms.Textarea(attrs={"rows": 1, "cols": 10}),
        # }