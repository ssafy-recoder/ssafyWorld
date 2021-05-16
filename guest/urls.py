from django.urls import path
from . import views

app_name = 'guest'
urlpatterns = [
    path('<int:pk>/', views.index, name='index'),
    path('<int:pk>/update/<int:article_pk>/', views.update, name='update'),
]
