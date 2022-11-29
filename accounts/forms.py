from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "volunteer_c",
            "area",
            "password1",
            "password2",
            "image",
        ]
        labels = {
            "volunteer_c": "이동봉사 여부",
            "area": "지역",
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            'area'
        ]