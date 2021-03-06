"""Posts URLs"""

# Django
from django.urls import path

# Views
from posts import views


urlpatterns = [
    path(
        route='posts/new/', 
        view= views.CreatePostView.as_view(), 
        name='create'
    ),
    
    path(
        route='', 
        view=views.PostFeedView.as_view(), 
        name='feed'
    ),
    
    path(
        route='posts/detail/<int:post_id>',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
]