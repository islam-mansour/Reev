from django.shortcuts import render

from .models import Offer


def index(request):
    offers = Offer.objects.filter(expired=False)
    context = {'offers': offers}
    return render(request, 'index.html', context)