from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('blog',views.blogs, name = "blog"),
    path('donate',views.donate, name = "donate"),
    path('recipe',views.recipe, name = "recipe"),
    path('food',views.food, name = "food"),
    path('food_card',views.food_card, name = "food_card"),
    path('int<id>',views.blog_detail,name = "blog_detail"),
    path('recipe_output',views.recipe_output, name = "recipe_output"),
    path('blogwrite',views.blogwrite, name = "blogwrite"),
]
