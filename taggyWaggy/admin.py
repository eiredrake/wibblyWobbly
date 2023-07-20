from django.forms import ModelForm
from nested_admin.nested import NestedModelAdmin
from django import forms
from taggyWaggy.models import Thingie
from django.contrib import admin


class ThingieAdminForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 50em;'}))

    class Meta:
        model = Thingie
        fields = '__all__'


# Register your models here.
@admin.register(Thingie)
class ThingieAdmin(NestedModelAdmin):
    list_display = ('name', 'tags')
    list_display_links = list_display
    ordering = list_display_links
    search_fields = list_display_links
    form = ThingieAdminForm
