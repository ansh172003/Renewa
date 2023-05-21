from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('congo',views.congo, name = "congo"),
    path('blog',views.blogs, name = "blog"),
    path('user_choice',views.user_choice, name = "user_choice"),

    path('donate',views.donate, name = "donate"),
    path('recipe',views.recipe, name = "recipe"),
    path('food',views.food, name = "food"),
    path('food_card',views.food_card, name = "food_card"),
    path('grocery_card',views.grocery_card, name = "grocery_card"),
    path('grocery/int<id>',views.singlegrocery,name = "singlegrocery"),

    path('int<id>',views.blog_detail,name = "blog_detail"),
    path('food/int<id>',views.singlefood,name = "singlefood"),
    path('recipe_output',views.recipe_output, name = "recipe_output"),
    path('blogwrite',views.blogwrite, name = "blogwrite"),
    
]
