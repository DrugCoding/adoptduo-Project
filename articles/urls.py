from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'articles'

urlpatterns = [
    path("", views.index, name="index"),
    path("dog/", views.dog_index, name="dog_index"),
    path("dog/create/", views.dog_create, name="dog_create"), # 입양글 작성
    path("dog/<int:dog_article_pk>/", views.dog_detail, name="dog_detail"), # 입양글 조회 페이지
    path("dog/<int:dog_article_pk>/update/", views.dog_update, name="dog_update"), # 입양글 수정
    path("dog/<int:dog_article_pk>/delete/", views.dog_delete, name="dog_delete"), # 입양글 삭제
    path("cat/", views.cat_index, name="cat_index"),
    path("cat/create/", views.cat_create, name="cat_create"), # 입양글 작성
    path("cat/<int:cat_article_pk>/", views.cat_detail, name="cat_detail"), # 입양글 조회 페이지
    path("<int:cat_article_pk>/update/", views.cat_update, name="cat_update"), # 입양글 수정
    path("<int:cat_article_pk>/delete/", views.cat_delete, name="cat_delete"), # 입양글 삭제
    path('<int:dog_article_pk>/dog/comments/', views.dog_comment_create, name='dog_comment_create'), # 댓글생성
    path('<int:cat_article_pk>/cat/comments/', views.cat_comment_create, name='cat_comment_create'),
    path("introduction/", views.introduction, name="introduction"),
]