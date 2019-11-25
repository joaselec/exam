from django import forms
from .models import itemCode
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class StockForm(forms.ModelForm):
    class Meta:
        model = itemCode
        fields = ('item',)