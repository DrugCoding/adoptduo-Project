from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

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
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '실명을 입력해주세요'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '추후 변경이 불가능 합니다'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'ex)user1004@cjstk.com'
                }
            ),
        }
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

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '아이디를 입력하세요'
#                 }
#             ),
#             'password': forms.PasswordInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '비밀번호를 입력하세요'
#                 }
#             )
#         }