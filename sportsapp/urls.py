from django.urls import path
from . import views

urlpatterns = [
    path('', views.league_list, name='league_list'),
    path('matches/<str:slug>/', views.league_matches, name='league_matches'),
    path('match/<str:slug>/', views.match_detail, name='match_detail'),
    path('robots.txt', views.robots_txt, name='ads-txt'),
]
