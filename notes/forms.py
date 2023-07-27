from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    # Define form fields for the 'title' and 'text' attributes of the 'Notes' model.

    # 'title' field with maximum length of 80 characters
    title = forms.CharField(max_length=80, label="Title", required=True)

    # 'text' field with maximum length of 500 characters, using a Textarea widget for multiline input
    text = forms.CharField(
        max_length=500,
        label="Your note",
        required=True,
        widget=forms.Textarea(attrs={"width": "100%", "rows": "5"})
    )

    class Meta:
        # Specify the 'Notes' model that this form is based on and the fields to be included in the form
        model = Notes
        fields = ["title", "text"]

