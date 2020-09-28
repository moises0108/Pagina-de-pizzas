"""Menu forms."""

# django
from django import forms
# utilities
from menu.models import Food


class MenuForm(forms.ModelForm):
    """Menu Model Form."""
    class Meta:
        """Forms settings."""
        model = Food
        fields = ('name', 'price', 'type_food')
