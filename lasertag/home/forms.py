from django.forms import ModelForm, formset_factory
from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'codename']
