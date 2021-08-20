from django import forms
from django.db.models import fields
from .models import Contact


class ContactMeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactMeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contact
        fields = ['name', 'Email', 'message']
