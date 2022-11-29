from django.urls import path
from . import views # 현재 같은 경로에 있는 views파일 참조

app_name = 'articles'

urlpatterns = [
    path("dog/", views.dog_index, name="dog_index"),
    path("dog/create/", views.dog_create, name="dog_create"), # 입양글 작성
    path("dog/<int:dog_article_pk>/", views.dog_detail, name="dog_detail"), # 입양글 조회 페이지
    path("dog/<int:dog_article_pk>/update/", views.dog_update, name="dog_update"), # 입양글 수정
    path("dog/<int:dog_article_pk>/delete/", views.dog_delete, name="dog_delete"), # 입양글 삭제
    path("cat/", views.cat_index, name="cat_index"),
    path("cat/create/", views.cat_create, name="cat_create"), # 입양글 작성
    # path("cat/<int:product_pk>/", views.catdetail, name="catdetail"), # 입양글 조회 페이지
    # path("<int:product_pk>/update/", views.update, name="update"), # 입양글 수정
    # path("<int:product_pk>/delete/", views.delete, name="delete"), # 입양글 삭제
]