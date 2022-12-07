from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.index, name ='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:pk>/comments/<int:c_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:pk>/bookmark/', views.bookmark, name="bookmark"), # 북마크
]