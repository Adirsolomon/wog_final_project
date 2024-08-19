from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_score, name='save_score'),
    path('restart/', views.save_and_restart, name='save_and_restart'), 
    path('scores/', views.view_scores, name='view_scores'), 
]
