from django.urls import path
#from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('addpost/', AddPostView.as_view(), name = 'addpost'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name = 'editpost'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name = 'deletepost'),
    path('addcategory/', AddCategoryView.as_view(), name = 'addcategory'),
    path('category/<str:cats>', CategoryView, name = 'category'),
    path('categorylist', CategoryListView, name = 'categorylist'),
    path('like/<int:pk>', LikeView, name='like_post'),
]