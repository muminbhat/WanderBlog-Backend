from django.urls import path
from .views import featured_blog, blog_post, blog_list, get_all_categories, get_blog_by_category

urlpatterns = [
    path('featured/', featured_blog, name='blogs'),
    path('all/', blog_list, name='blogs'),
    path('<str:slug>/', blog_post, name='blogpost'),
    path('categories/all/', get_all_categories, name='all_categories'),
    path('category/<int:category_id>/', get_blog_by_category, name='blg-by-category'),


]
