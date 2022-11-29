from django import forms
from .models import DogArticle, CatArticle

class DogArticleForm(forms.ModelForm):
        class Meta:
            model = DogArticle
            exclude = (
                "bookmarks",
                "hits",
                "user",
            )

class CatArticleForm(forms.ModelForm):
        class Meta:
            model = CatArticle
            exclude = (
                "bookmarks",
                "hits",
                "user",
            )