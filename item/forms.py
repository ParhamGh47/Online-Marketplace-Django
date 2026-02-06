from django import forms
from .models import Item

INPUT_CLASS = (
    "w-full py-4 px-5 rounded-xl "
    "bg-[#0b0f14] text-gray-200 "
    "border border-teal-900 "
    "placeholder-gray-500 "
    "focus:outline-none focus:border-teal-500 "
    "focus:ring-2 focus:ring-teal-500/30 "
    "transition"
)

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS + " file:bg-teal-500 file:text-black file:border-0"
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS + " file:bg-teal-500 file:text-black file:border-0"
            }),
        }
