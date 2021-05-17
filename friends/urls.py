from django.urls import path
from . import views

app_name = 'friends'
urlpatterns = [
    path('<username>/', views.index, name='index'),
    path('<username>/recommend', views.recommend, name='recommend'),
    path('<username>/location', views.location, name='location'),
    path('<username>/save_location/', views.save_location, name='save_location'),
]