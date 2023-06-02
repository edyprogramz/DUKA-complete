from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input field"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "input field"
    }))
    price = forms.FloatField(widget=forms.TextInput(attrs={
        "class": "input field"
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "input field"
    }))

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'is_sold')
        
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input field"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "input field"
    }))
    price = forms.FloatField(widget=forms.TextInput(attrs={
        "class": "input field"
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "input field"
    }))
    
