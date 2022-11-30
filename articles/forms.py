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
    class Meta:
        model = CatArticle
        exclude = (
            "bookmarks",
            "hits",
            "user",
        )

class DogCommentForm(forms.ModelForm):
    class Meta:
        model = DogArticleComment 
        fields = ['content',]

class CatCommentForm(forms.ModelForm):
    class Meta:
        model = CatArticleComment 
        fields = ['content',]