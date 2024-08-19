from django.urls import path
from game import views

urlpatterns = [
    path('', views.play, name='play'),
    path('check/', views.check_guess, name='check_guess'),
    path('quit/', views.quit_game, name='quit_game'),
]
