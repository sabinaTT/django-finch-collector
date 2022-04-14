from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name='home'), # here we have added the new path!
    path('about/', views.About.as_view(), name='about'),
    path('index/', views.Index.as_view(), name='index'),
    path('finches/', views.Finch_List.as_view(), name='finch_list'),
    path('finches/new', views.Finch_Create.as_view(), name='finch_create'),
    path('finches/<int:pk>/', views.Finch_Detail.as_view(), name='finch_detail'),
    path('finches/<int:pk>/update', views.Finch_Update.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete', views.Finch_Delete.as_view(), name='finch_delete'),
    path('user/<username>', views.profile, name='profile'),
    path('birdhouses/', views.birdhouses_index, name='birdhouses_index'),
    path('birdhouses/<int:birdhouse_id>', views.birdhouses_show, name='birdhouses_show'), 
    path('birdhouses/create', views.BirdHouseCreate.as_view(), name='birdhouses_create'),
    path('birdhouses/<int:pk>/update/', views.BirdHouseUpdate.as_view(), name='birdhouses_update'),
    path('birdhouses/<int:pk>/delete/', views.BirdHouseDelete.as_view(), name='birdhouses_delete'),
]