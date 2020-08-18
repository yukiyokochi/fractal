from django.urls import path
from . import views
from .views import CategoryListView, BlogCategoryList, CategoriesListView, CommentCreate, SearchListView

app_name='blog'

urlpatterns = [
    path('',views.CategoryListView.as_view(), name='top'),
    path('categories/<int:pk>/',views.BlogCategoryList.as_view(),name='category_list'),
    path('categories/',views.CategoriesListView.as_view(),name='categories'),
    path('detail/<int:pk>/',views.detail,name='blog_detail'),
    # path('detail/<int:pk>/like/',views.like,name="like"),
    # path('api/like/<int:pk>/', views.api_like, name="api_like"),
    path('create/',views.blog_create,name='blog_create'),
    path('comment/<int:pk>/',views.CommentCreate.as_view(),name='comment_create'),
    path('search/',views.SearchListView.as_view(),name='search'),
    path('recommend/',views.RecommendListView.as_view(),name='recommend'),
]
