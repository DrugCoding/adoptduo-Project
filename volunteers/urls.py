from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.index, name ='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:pk>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/bookmark/', views.bookmark, name='bookmark'),
]