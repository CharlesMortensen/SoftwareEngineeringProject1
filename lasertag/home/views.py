from django.http import HttpResponse
from django.shortcuts import render
from .forms import PlayerForm
from django.forms import formset_factory

def index(request):
    return render(request, 'home/index.html')
    
def player_entry(request):

    RedPlayerFormSet = formset_factory(PlayerForm, extra=19)
    BluePlayerFormSet = formset_factory(PlayerForm, extra=19)

    red_player_formset = RedPlayerFormSet(prefix="red")
    blue_player_formset = BluePlayerFormSet(prefix="blue")

    return render(request, 'home/player_entry.html', {'title': 'Player Entry', 'red_player_formset': red_player_formset, 'blue_player_formset': blue_player_formset})