from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player_entry', views.player_entry, name='player_entry'),
]