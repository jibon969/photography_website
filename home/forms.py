from django import forms
from .models import Photo
from ckeditor.widgets import CKEditorWidget


class UploadFileForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Post title here '}))
    description = forms.CharField(widget=CKEditorWidget(attrs={'placeholder': 'Descriptions'}))

    class Meta:
        model = Photo
        fields = ['title', 'image', 'description']
