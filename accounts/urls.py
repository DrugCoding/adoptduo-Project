from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("", views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path("update/", views.update, name="update"),
    path("change_password/", views.change_password, name="change_password"),
    path("delete/", views.delete, name="delete"),
    path("<int:pk>/follow/", views.follow, name="follow"),
    # path("login/kakao/", views.kakao_login, name="kakao-login"),
    # path("login/kakao/callback/", views.kakao_login_callback, name="kakao-callback"),
]