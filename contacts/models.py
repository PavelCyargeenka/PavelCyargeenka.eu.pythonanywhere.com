from django.core.validators import MinLengthValidator
from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=20, null=False, validators=[MinLengthValidator(3)])
    e_mail = models.EmailField(default='')
    message = models.TextField(max_length=180, null=False)
