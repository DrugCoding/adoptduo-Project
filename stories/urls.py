from django.urls import path
from . import views

app_name = "stories"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:pk>/comments/<int:storycomment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:stories_pk>/likes/', views.likes, name="likes"),
]