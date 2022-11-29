from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'articles'

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"), # 입양글 작성
    path("<int:product_pk>/", views.detail, name="detail"), # 입양글 조회 페이지
    path("<int:product_pk>/update/", views.update, name="update"), # 입양글 수정
    path("<int:product_pk>/delete/", views.delete, name="delete"), # 입양글 삭제
    # 강아지페이지(임시)
    path("dog/", views.dog, name="dog"),
    # 고양이페이지(임시)
    path("cat/", views.cat, name="cat"),
]