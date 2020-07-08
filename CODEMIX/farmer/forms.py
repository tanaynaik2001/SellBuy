from django import forms
from .models import addCrop

class addCropForm(forms.ModelForm):
    class Meta:
        model = addCrop
        fields = ('addCropName', 'addCropPrice', 'addCropImg','addCropDescription','addCropQuantity', 'addFarmerID')