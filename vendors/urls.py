from django.urls import path, include
from . import views

urlpatterns = [
    path('sell_food',views.sell_food, name = "sell_food"),
    path('dashboard',views.dashboard, name = "dashboard")
]
