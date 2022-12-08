from django import forms
from .models import DogArticle, CatArticle, DogArticleComment, CatArticleComment

class DogArticleForm(forms.ModelForm):
    gender_list = [
        ('암컷', '암컷'),
        ('수컷', '수컷'), 
    ]
    gender = forms.ChoiceField(choices=gender_list, 
        widget=forms.RadioSelect(
        ),
    )

    
    class Meta:
        model = DogArticle
        exclude = (
            "bookmarks",
            "hits",
            "user",
        )
 





class CatArticleForm(forms.ModelForm):
    gender_list = [
        ('암컷', '암컷'),
        ('수컷', '수컷'), 
    ]
    gender = forms.ChoiceField(choices=gender_list, 
        widget=forms.RadioSelect(
        ),
    )
    # title = forms.TextInput(
    #     widget=forms.TextInput
    #     attrs={'placeholder': '제목을 입력해주세요',
    #     }
    # )

    class Meta:
        model = CatArticle
        exclude = (
            "bookmarks",
            "hits",
            "user",
        )
        # fields = {
        #     "title", "cat_breed"
        # }


class DogCommentForm(forms.ModelForm):
    class Meta:
        model = DogArticleComment 
        fields = ['content',]
        labels = {
            "content": "댓글입력",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 1, "cols": 10}),
        }

class CatCommentForm(forms.ModelForm):
    class Meta:
        model = CatArticleComment 
        fields = ['content',]
        labels = {
            "content": "댓글입력",
        }
        widgets = {
            "content": forms.Textarea(attrs={"rows": 1, "cols": 10}),
        }