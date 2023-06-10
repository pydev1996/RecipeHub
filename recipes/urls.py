from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('user', views.user_recipe_list, name='user_recipe_list'),
    path('user/user_recipe', views.user_recipes, name='user_recipes'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),
    path('recipe/<int:pk>/chat/', views.send_chat_message, name='send_chat_message'),


]
