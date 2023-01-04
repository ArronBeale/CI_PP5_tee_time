# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_address1': 'Street Address 1',
            'default_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }
        aria_labels = {
            'default_phone_number': 'Phone number for the user',
            'default_postcode': 'Postal code for the user',
            'default_town_or_city': 'Town or city for the user',
            'default_address1': 'Street address 1 for the user',
            'default_address2': 'Street address 2 for the user',
            'default_county': 'County, state, or locality for the user',
        }
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['aria-label'] = aria_labels[
                    field
                ]
                self.fields[field].label = placeholders[field]
            else:
                self.fields[field].label
