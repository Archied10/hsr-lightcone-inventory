from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "rarity", "lc_path", "base_atk", "base_hp", "base_def"]