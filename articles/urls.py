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
    path("information/declaration/", views.info_declartation, name="info_declartation"),
    path("information/", views.information, name="information"),
    path("information/adopt/", views.info_adopt, name="info_adopt"),
    path('<int:dog_article_pk>/comments/<int:dog_comment_pk>/dog/delete/', views.dog_comments_delete, name='dog_comments_delete'),
    path('<int:cat_article_pk>/comments/<int:cat_comment_pk>/cat/delete/', views.cat_comments_delete, name='cat_comments_delete'),
    path('<int:dog_article_pk>/dog/bookmark/', views.dog_bookmark, name="dog_bookmark"), # 북마크
    path("search/", views.search, name="search"), # 검색기능
    path('<int:cat_article_pk>/cat/bookmark/', views.cat_bookmark, name="cat_bookmark"), 
    path("<int:cat_category_pk>/cat/category/", views.cat_category, name="cat_category"),
    path("<int:dog_category_pk>/dog/category/", views.dog_category, name="dog_category"),
]