from django.urls import path
from . import views

urlpatterns = [
    path('', views.play, name='play'),
    path('check/', views.check_memory, name='check_memory'),
    path('quit/', views.quit_game, name='quit_game'),
]

