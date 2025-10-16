from django import forms
from .utils import luhn_checksum_is_valid

class CardCheckForm(forms.Form):
    number = forms.CharField(
        label="Numéro de carte",
        widget=forms.TextInput(attrs={
            "class": "w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        }),
        max_length=19
    )

    def clean_number(self):
        number = self.cleaned_data["number"].replace(" ", "").replace("-", "")
        if not number.isdigit():
            raise forms.ValidationError("Le numéro doit contenir uniquement des chiffres.")
        if not luhn_checksum_is_valid(number):
            raise forms.ValidationError("Numéro invalide selon l'algorithme de Luhn.")
        return number
