from Zipam import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import ContactForm


@csrf_exempt
def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_nume = request.POST.get('nume')
        form_telefon = request.POST.get('telefon')
        form_oras = request.POST.get('oras')
        form_email = request.POST.get('email')
        form_mesaj = request.POST.get('mesaj')

        contact_mesaj = "%s:%s,%s,%s via %s" % (
            form_nume,
            form_telefon,
            form_oras,
            form_email,
            form_mesaj
        )

        subiect = 'Mesaj de pe Ferestre Zipam'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = settings.EMAIL_HOST_USER

        try:
            send_mail(subiect, contact_mesaj, from_email, to_email, fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        messages.success(request, 'Mesajul a fost trimis!')

    return render(request, 'index.html', {'form': form})
