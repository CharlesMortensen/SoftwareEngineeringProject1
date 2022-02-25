from django.http import HttpResponse
from django.shortcuts import render
from .forms import PlayerForm
from django.forms import formset_factory

def index(request):
    return render(request, 'home/index.html')
    
def player_entry(request):
    """if request.method == 'POST':
        formset = PlayerFormSet(request.POST)

    else:
        formset = PlayerFormSet()"""
    PlayerFormSet = formset_factory(PlayerForm, extra=19)

    return render(request, 'home/player_entry.html', {'title': 'Player Entry', 'formset': PlayerFormSet})