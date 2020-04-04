from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Note


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model  = Note
        fields = ['title' , 'content' , 'tags']