from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.index, name ='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:pk>/delete_comment/', views.comment_delete, name='comment_delete'),
    path('<int:pk>/bookmark/', views.bookmark, name="bookmark"), # 북마크
]