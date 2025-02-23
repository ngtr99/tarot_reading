from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .models import TarotCard, Career, Love, Health, Finance
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


def career(request):
    career_cards = Career.objects.all()  # Get all Career objects 
    return render(request, 'catalog.html', {
        'content': 'Career',
        'catalog': random.sample(list(career_cards), len(career_cards)),  # Shuffled career cards
    })


def love(request):
    love_cards = Love.objects.all()  # Get all Career objects

    return render(request, 'catalog.html', {
        'content': 'Love',
        'catalog': random.sample(list(love_cards), len(love_cards)),
    })

def health(request):
    health_cards = Health.objects.all()  # Get all Career objects

    return render(request, 'catalog.html', {
        'content': 'Health',
        'catalog':  random.sample(list(health_cards), len(health_cards)),
    })

def finance(request):
    finance_cards = Finance.objects.all()  # Get all Finance objects

    return render(request, 'catalog.html', {
        'content': 'Finance',
        'catalog': random.sample(list(finance_cards), len(finance_cards)),
    })


def reading(request,slug1, slug2):
    if slug1 == 'Career':
        card = Career.objects.all().get(tarot_card__name=slug2)
    elif slug1 == 'Love':
        card = Love.objects.all().get(tarot_card__name=slug2)
    elif slug1 == 'Health':
        card = Health.objects.all().get(tarot_card__name=slug2)
    elif slug1 == 'Finance':
        card = Finance.objects.all().get(tarot_card__name=slug2)

    return render(request, 'reading.html', {
        'content': slug1,
        'card': card,
    })