from django import forms
from notes import models


class TextForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": 'Название заметки'}),
        max_length=100,
        required=True
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": 'Введите markdown...'}),
        max_length=50000,
        required=True
    )


class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['file']
