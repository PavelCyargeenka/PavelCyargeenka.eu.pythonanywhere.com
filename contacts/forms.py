from django import forms
from contacts.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        labels = {
            'name': 'Name:',
            'e_mail': 'E-mail:',
            'message': 'Message:'
        }


