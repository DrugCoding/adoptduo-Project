from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate
from accounts.exception import SocialLoginException, KakaoException
import requests
import datetime
from .models import User
import os
from django.http import JsonResponse


def index(request):
    accounts = get_user_model().objects.order_by("-pk")
    context = {"accounts": accounts}
    return render(request, "accounts/index.html", context)

def signup(request):
    if request.method == 'POST':
        # print(request.FILES) #체크
        form = CustomUserCreationForm(request.POST, request.FILES)
        # print(form) #체크
        if form.is_valid():
            # print(request.FILES) #체크
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:   
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# def kakao_login(request):
#     try:
#         if request.user.is_authenticated:
#             raise SocialLoginException("User already logged in")
#         client_id = os.getenv("REACT_APP_KAKAO_REST_API_KEY")
#         redirect_uri = "http://localhost:8000/accounts/login/kakao/callback/"

#         return redirect(
#             f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
#         )
#     except KakaoException as error:
#         messages.error(request, error)
#         return redirect("articles:index")
#     except SocialLoginException as error:
#         messages.error(request, error)
#         return redirect("articles:index")

# def kakao_login(request):
#     client_id = os.environ.get("REACT_APP_KAKAO_REST_API_KEY")
#     REDIRECT_URI = "http://localhost:8000/accounts/login/kakao/callback/"
#     return redirect(
#         f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code")

# class KakaoException(Exception): # 👈 에러처리를 위해 class 생성
#     pass

# def kakao_login_callback(request):
#     try:
#     	#(1)
#         code = request.GET.get("code")
#         client_id = os.environ.get("REACT_APP_KAKAO_REST_API_KEY")
#         REDIRECT_URI = "http://localhost:8000/accounts/login/kakao/callback/"
#         #(2)
#         token_request = requests.get(
#             f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={REDIRECT_URI}&code={code}"
#         )
#         #(3)
#         token_json = token_request.json()
#         error = token_json.get("error", None)
#         if error is not None:
#             raise KakaoException()
#         #(4)
#         access_token = token_json.get("access_token")
#         #(5)
#         profile_request = requests.get(
#             "https://kapi.kakao.com/v2/user/me",
#             headers={"Authorization": f"Bearer {access_token}"},
#         )
#         profile_json = profile_request.json()
#         #(6)
#         email = profile_json.get("kakao_account", None).get("email")
#         if email is None:
#             raise KakaoException()
#         properties = profile_json.get("properties")
#         nickname = properties.get("nickname")
#         profile_image = properties.get("profile_image")
#         #(7)
#         try:
#             user = User.objects.get(email=email)
#             if user.login_method != User.LOGIN_KAKAO:
#                 raise KakaoException()
#         except User.DoesNotExist:
#             user = User.objects.create(
#                 email=email,
#                 username=email,
#                 first_name=nickname,
#                 login_method=User.LOGIN_KAKAO,
#                 email_verified=True,
#             )
#             user.set_unusable_password()
#             user.save()
#             #(8)
#             if profile_image is not None:
#                 photo_request = requests.get(profile_image)
#                 user.avatar.save(
#                     f"{nickname}-avatar", ContentFile(photo_request.content)
#                 )
#         login(request, user)
#         return redirect(reverse("articles:index"))
#     except KakaoException:
#         return redirect(reverse("accounts:login"))

# def kakao_login_callback(request):
#     try:
#         if request.user.is_authenticated:
#             raise SocialLoginException("User already logged in")
#         code = request.GET.get("code", None)
#         if code is None:
#             KakaoException("Can't get code")
#         client_id = os.getenv("REACT_APP_KAKAO_REST_API_KEY")
#         redirect_uri = "http://localhost:8000/accounts/login/kakao/callback/"
#         client_secret = os.getenv("REACT_APP_KAKAO_CLIENT_API_KEY")
#         request_access_token = requests.post(
#             f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}&client_secret={client_secret}",
#             headers={"Accept": "application/json"},
#         )
#         access_token_json = request_access_token.json()
#         error = access_token_json.get("error", None)
#         if error is not None:
#             print(error)
#             KakaoException("Can't get access token")
#         access_token = access_token_json.get("access_token")
#         headers = {"Authorization": f"Bearer {access_token}"}
#         profile_request = requests.post(
#             "https://kapi.kakao.com/v2/user/me",
#             headers=headers,
#         )
#         profile_json = profile_request.json()
#         kakao_account = profile_json.get("kakao_account")
#         profile = kakao_account.get("profile")

#         nickname = profile.get("nickname", None)
#         avatar_url = profile.get("profile_image_url", None)
#         email = kakao_account.get("email", None)
#         gender = kakao_account.get("gender", None)

#         user = get_user_model().objects.get_or_none(email=email)
#         if user is not None:
#             if user.login_method != get_user_model().LOGIN_KAKAO:
#                 raise GithubException(f"Please login with {user.login_method}")
#         else:
#             user = get_user_model().objects.create_user(
#                 email=email,
#                 username=email,
#                 first_name=nickname,
#                 gender=gender,
#                 login_method=get_user_model().LOGIN_KAKAO,
#             )

#             if avatar_url is not None:
#                 avatar_request = requests.get(avatar_url)
#                 user.avatar.save(
#                     f"{nickname}-avatar", ContentFile(avatar_request.content)
#                 )
#             user.set_unusable_password()
#             user.save()
#         messages.success(request, f"{user.email} signed up and logged in with Kakao")
#         login(request, user)
#         return redirect(reverse("articles:index"))
#     except KakaoException as error:
#         messages.error(request, error)
#         return redirect(reverse("articles:index"))
#     except SocialLoginException as error:
#         messages.error(request, error)
#         return redirect(reverse("articles:index"))

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect("accounts:login")

@login_required
def follow(request, pk):
    if request.user.is_authenticated:
        Users = get_user_model()
        me = request.user
        you = Users.objects.get(pk=pk)
        if me != you:
            if me in you.followers.all():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                "is_followed": is_followed,
                "followers_count": you.followers.count(),
                "followings_count": you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:detail', you.username)
    return redirect('accounts:login')



# @login_required
# def follow(request, pk):
#     accounts = get_user_model().objects.get(pk=pk)
#     if request.user == accounts:
#         return redirect("accounts:detail", pk)
#     if request.user in accounts.followers.all():
#         accounts.followers.remove(request.user)
#     else:
#         accounts.followers.add(request.user)
#     return redirect("accounts:detail", pk)

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("accounts:detail", request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:index")

# def __init__(self, *args, **kwargs):
#     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#     self.fields['username'].widget.attrs['placeholder'] = "추후 수정이 불가능 합니다"