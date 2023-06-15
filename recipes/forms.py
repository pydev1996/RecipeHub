# forms.py
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'ingredients', 'description', 'processtime','image', 'audio','category','youtube_links')
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }

