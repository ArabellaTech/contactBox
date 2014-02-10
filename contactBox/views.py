# -*- coding: utf-8 -*-
from forms import ContactForm
from django.contrib import messages


def contact_form(request):
    """
    Return form object and status of saving
    """
    form = ContactForm()
    saved = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        saved = True
        messages.add_message(request, messages.INFO, 'Your message has been sent.')
    return {'form': form, 'saved': saved}
