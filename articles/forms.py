from django import forms
from .models import DogArticle, CatArticle, DogArticleComment, CatArticleComment
class DogArticleForm(forms.ModelForm):
    # gender_list = [
    #     ('암컷', '암컷'),
    #     ('수컷', '수컷'), 
    # ]
    # gender = forms.ChoiceField(choices=gender_list, 
    #     widget=forms.RadioSelect(
    #     ),
    # )

    
    class Meta:
        model = DogArticle
        exclude = (
            "bookmarks",
            "hits",
            "user",
            "lat",
            "lng",
        )
        fields = (
            "title",
            "name",
            "location",
            "content",
            "image",
            "age",
            "gender",
            "dog_breed",
            "memo",
            "neutered",
            "vaccination",
        )
        labels = {
            "title": "🗒️게시글",
            "name": "🏷️이름",
            "location": "🌏지역",
            "content": "🖋️게시물 내용",
            "image": "📷사진",
            "age": "🔢나이",
            "gender": "성별",
            "dog_breed": "🐶견종",
            "memo": "📝특이사항",
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
                    "placeholder": "강아지의 이름을 입력해주세요.",
                }),
            "location": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "지역을 입력해주세요.",
                }),
            "content": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "게시물의 내용을 작성해주세요.",
                }),
            "age": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "나이를 입력해주세요.",
                }),
            "gender": forms.RadioSelect(
                choices = [
                    ('암컷', '암컷'),
                    ('수컷', '수컷'),
                ],
            ),
            "memo": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "특이사항을 입력해주세요.",
                }),
        }
        
 

class CatArticleForm(forms.ModelForm):
    # gender_list = [
    #     ('암컷', '암컷'),
    #     ('수컷', '수컷'), 
    # ]
    # 성별 = forms.ChoiceField(choices=gender_list, 
    #     widget=forms.RadioSelect(
    #     ),
    # )

    class Meta:
        model = CatArticle
        exclude = (
            "bookmarks",
            "hits",
            "user",
            "lat",
            "lng",
        )
        fields = (
            "title",
            "name",
            "location",
            "content",
            "image",
            "age",
            "gender",
            "cat_breed",
            "memo",
            "neutered",
            "vaccination",
        )
        labels = {
            "title": "🗒️게시글",
            "name": "🏷️이름",
            "location": "🌏지역",
            "content": "🖋️게시물 내용",
            "image": "📷사진",
            "age": "🔢나이",
            "gender": "성별",
            "cat_breed": "😺묘종",
            "memo": "📝특이사항",
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
                    "placeholder": "고양이의 이름을 입력해주세요.",
                }),
            "location": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "지역을 입력해주세요.",
                }),
            "content": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "게시물의 내용을 작성해주세요.",
                }),
            "age": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "나이를 입력해주세요.",
                }),
            "gender": forms.RadioSelect(
                choices = [
                    ('암컷', '암컷'),
                    ('수컷', '수컷'),
                ],
            ),
            "memo": forms.TextInput(
                attrs={
                    "class": "hover-control",
                    "placeholder": "특이사항을 입력해주세요.",
                }),
        }


class DogCommentForm(forms.ModelForm):
    class Meta:
        model = DogArticleComment 
        fields = ['content',]
        labels = {
            "content": " ",
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