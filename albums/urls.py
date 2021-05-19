from django.urls import path
from . import views

app_name = 'albums'
urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
    path('<int:pk>/create/', views.create, name='create'),
    path('<int:pk>/photo/', views.photo, name='photo'),
    path('<int:pk>/delete/', views.delete, name="delete"),

    path('<int:pk>/comments/', views.comments_create, name='comments_create'),


    # path('category/', views.category, name='category'),
    
    
]
