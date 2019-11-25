from django import forms
from .models import board
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BoardForm(forms.ModelForm):
    class Meta:
        model = board
        fields = ('title', 'detail',)