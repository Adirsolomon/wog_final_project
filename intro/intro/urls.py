from django.urls import path, include
from welcome import views as welcome_views

urlpatterns = [
    path('', welcome_views.welcome, name='welcome'),
    
]
