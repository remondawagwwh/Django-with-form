from django import forms
from django.core.validators import FileExtensionValidator
from .models import *
class ProductForm(forms.Form):
    name= forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Enter product name'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter product description'})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'placeholder': 'e.g. 199.99'})
    )
    stock = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'e.g. 20'})
    )
    sku = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Unique SKU'})
    )
    image = forms.ImageField(
        label='Product Image',
        required=False,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        widget=forms.FileInput(attrs={'accept': 'image/jpeg,image/png'})
    )
    # category = forms.ChoiceField(
    #     choices=[(cat.id, cat.name) for cat in Category.getall()],
    #     widget=forms.Select()
    # )
    category = forms.ChoiceField(choices=[])

class ProductFormModel(forms.Form):
    class Meta:
        model=Product
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize widgets
        self.fields['image'].widget.attrs.update({'accept': 'image/*'})
        self.fields['category'].choices = [(cat.id, cat.name) for cat in Category.getall()]
        self.fields['date_added'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['date_updated'].widget = forms.DateInput(attrs={'type': 'date'})

