from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from contacts.forms import ContactForm


class Success(TemplateView):
    template_name = 'contacts/success.html'


class Contacts(FormView):
    form_class = ContactForm
    success_url = '/success/'
    template_name = 'contacts/contacts.html'

    def form_valid(self, form):
        form.save()
        try:
            send_mail(
                subject='New message from your Deep Purple website user form',
                message=f'''
                Name: {form.cleaned_data['name']}\n\n
                E-mail: {form.cleaned_data['e_mail']}\n\n
                Message: {form.cleaned_data['message']}\n
                ''',
                from_email='infodjango47@gmail.com',
                recipient_list=['pavelcyargeenka@gmail.com'],
                fail_silently=True
            )

            send_mail(
                subject='This is an automatically generated email – please do not reply to it',
                message=f'Thank you for your message! We will contact you as soon as possible.\n\n',
                from_email='infodjango47@gmail.com',
                recipient_list=[form.cleaned_data['e_mail']],
                fail_silently=True
            )

        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return super(Contacts, self).form_valid(form)
