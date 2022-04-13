from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'), # here we have added the new path!
    path('about/', views.About.as_view(), name='about'),
    path('index/', views.Index.as_view(), name='index'),
    path('finches/', views.Finch_List.as_view(), name='finch_list'),
]