# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django import forms
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Product, Category
from .widgets import CustClearableFileInput
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories_list = Category.objects.all()
        friendly_names = [
            (c.id, c.get_friendly_name()) for c in categories_list
            ]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-secondary rounded'
