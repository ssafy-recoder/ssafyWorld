from django.urls import path
from . import views


app_name = 'homepage'
urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
    path('test/', views.test),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
