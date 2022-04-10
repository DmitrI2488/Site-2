from django.core.paginator import Paginator
from django.shortcuts import render
from Home.models import rating


def ratings(request):
    alla = rating.objects.all()
    rat = Paginator(rating.objects.all(), 8)
    page = request.GET.get('page')
    chanels = rat.get_page(page)
    return render(request, 'rating/rating.html',
                  {'chanels': chanels,
                   'chanel': alla})


def failed(request):
    rat = Paginator(rating.objects.all(), 8)
    page = request.GET.get('page')
    chanels = rat.get_page(page)
    return render(request, 'rating/failed.html',
                  {'chanels': chanels})
