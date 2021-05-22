from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('allsongs', views.allsongs, name="allsongs"),
    path('allsongs/<int:id>', views.songpost, name="songpost"),
    path('signup', views.signup ,name="signup"),
    path('login', views.loginpage  , name="loginpage"),
    path('logout', views.logoutuser  , name="logout"),
    path('listenlater', views.listenlater  , name="listenlater"),
    path('history', views.history  , name="history"),
    path('search', views.search  , name="search"),

]
