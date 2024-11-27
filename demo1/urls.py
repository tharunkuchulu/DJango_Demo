from django.urls import path
from . import views

urlpatterns = [
    path('demo1/greet/', views.greet, name='greet'),
    path('demo1/message/', views.message, name='message')
]

