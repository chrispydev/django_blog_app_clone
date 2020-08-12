from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post-create', views.PostCreateView.as_view(), name='post_create'),
]
