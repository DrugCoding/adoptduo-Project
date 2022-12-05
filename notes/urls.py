from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'notes'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/send/", views.send, name="send"),
]