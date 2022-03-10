from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player_entry', views.player_entry, name='player_entry'),
    path('game_action', views.game_action, name='game_action'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)