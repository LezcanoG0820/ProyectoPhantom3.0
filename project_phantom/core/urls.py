from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("register/", views.register, name="register"),
  path("logout/", views.logout_view, name="logout"),
  path('game_categories/', views.game_categories, name='game_categories'),
  path('game_categories/create/', views.create_game_category, name='create_game_category'),
  path('game_categories/edit/<int:pk>/', views.edit_game_category, name='edit_game_category'),
  path('game_categories/delete/<int:pk>/', views.delete_game_category, name='delete_game_category'),

]