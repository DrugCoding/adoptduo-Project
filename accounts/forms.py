from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "name",
            "username",
            "area",
            "volunteer_c",
            "email",
            "password1",
            "password2",
            "image",
        )
        labels = {
            "name": "이름",
            "username": "아이디",
            "area": "거주지역",
            "volunteer_c": "이동봉사 여부",
            "email": "이메일",
            "image": "이미지 파일",
        }
        # widgets = {
        #     'username': UserCreationForm(attrs={'placeholder': '추후 수정불가'}),
        # }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "name",
            "area",
            "volunteer_c",
            "email",
            "image",
        )
        labels = {
            "name": "이름",
            "area": "거주지역",
            "volunteer_c": "이동봉사 여부",
            "email": "이메일",
            "image": "이미지 파일",
        }