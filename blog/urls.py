from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post-create', views.PostCreateView.as_view(), name='post_create'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post-delete/<int:pk>/delete',
         views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post_update'),

]
