from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .forms import FlashCardForm
from .models import FlashCard

import random


def main(request, position=None):
    cards = FlashCard.objects.all()
    total = len(cards)
    if position is None:
        if 'position' in request.session:
            position = request.session['position']
        else:
            position = 0
            request.session['position'] = position
        return redirect(f'/{position}')
    try:
        position = int(position)
    except ValueError:
        return redirect('/0')
    if position < 0:
        return redirect('/0')
    if 'card_ids' in request.session:
        card_ids = request.session['card_ids']
        if total > len(card_ids):
            for i, card in enumerate(cards):
                if i >= len(card_ids):
                    request.session['card_ids'].append(card.id)
    else:
        card_ids = [card.id for card in cards]
        request.session['card_ids'] = card_ids
    try:
        card = cards.get(id=card_ids[position])
    except IndexError:
        return redirect('/0')
    context = {
        'card': card,
        'position': position,
        'total': total
    }
    return render(request, 'card.html', context)


def edit(request):
    if not request.user.is_authenticated:
        raise Http404('You don\'t have permission to edit cards')
    cards = FlashCard.objects.all().order_by('cue')
    if request.method == 'POST':
        form = FlashCardForm(request.POST)
        if form.is_valid():
            card_dict = {
                'category': form.cleaned_data['category'],
                'cue': form.cleaned_data['cue'],
                'cue_expanded': form.cleaned_data['cue_expanded'],
                'info': form.cleaned_data['info']
            }
            card_id = form.cleaned_data['id']
            if card_id:
                FlashCard.objects.filter(id=card_id).update(**card_dict)
            else:
                flashcard = FlashCard.objects.create(**card_dict)
                flashcard.save()
            return HttpResponse(f'{card_dict["cue"]} Saved!')
        else:
            return HttpResponse('Error!')
    else:
        form = FlashCardForm()
    context = {
        'form': form,
        'cards': cards
    }
    return render(request, 'card_edit.html', context)


def shuffle(request):
    cards = list(FlashCard.objects.all())
    request.session['card_ids'] = []
    request.session['position'] = 0
    random.shuffle(cards)
    for card in cards:
        request.session['card_ids'].append(card.id)
    return redirect('/0')
