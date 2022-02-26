from django.http import HttpResponse
from django.shortcuts import render
from .forms import PlayerForm
from django.forms import formset_factory

def index(request):
    return render(request, 'home/index.html')
    
def player_entry(request):

    RedPlayerFormSet = formset_factory(PlayerForm, extra=19)
    BluePlayerFormSet = formset_factory(PlayerForm, extra=19)
    #manage_data with these params is required for each
    manage_data_red = { 'red-TOTAL_FORMS': '20', 'red-INITIAL_FORMS': '0',}
    manage_data_blue = { 'blue-TOTAL_FORMS': '20', 'blue-INITIAL_FORMS': '0',}
    red_player_formset = RedPlayerFormSet(manage_data_red, prefix="red")
    blue_player_formset = BluePlayerFormSet(manage_data_blue, prefix="blue")

    if request.method == 'POST':
        # separate the red form data from the blue form data
        post_data_red = {}
        post_data_blue = {}
        for key in request.POST:
            if "red-" in key:
                post_data_red[key] = (request.POST)[key]
            elif "blue-" in key:
                post_data_blue[key] = (request.POST)[key]
        # make a formset for the 2 forms. must pass them the right prefix so that it knows to take it off for the save()
        post_formset_red = RedPlayerFormSet(post_data_red, prefix="red")
        post_formset_blue = BluePlayerFormSet(post_data_blue, prefix="blue")
        # must validate data otherwise it won't clean it and create the cleaned_data member for save()
        post_formset_red.is_valid()
        post_formset_blue.is_valid()
        # for both formsets need to loop through each form to save individual forms
        for form in post_formset_red:
            if form.is_valid() and form.cleaned_data: #form must be valid and non-empty before saving
                form.save()
        for form in post_formset_blue:
            if form.is_valid() and form.cleaned_data: #form must be valid and non-empty before saving
                form.save()

    return render(request, 'home/player_entry.html', {'title': 'Player Entry', 'red_player_formset': red_player_formset, 'blue_player_formset': blue_player_formset})