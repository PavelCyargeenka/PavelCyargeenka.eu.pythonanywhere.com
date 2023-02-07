from django.contrib import admin
from contacts.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'e_mail', 'message']
    list_editable = ['name', 'e_mail', 'message']
    ordering = ['id']

