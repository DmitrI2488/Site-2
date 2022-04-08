from django.shortcuts import render

from Home.models import rating

from django.core.paginator import Paginator


def show_chanel(request, chanel_id):
    chanel = rating.objects.get(pk=chanel_id)
    return render(request, 'Home/show_chanel.html', {
        'chanel': chanel
    })


def all_events(request):
    rating_list = rating.objects.all()
    for ratings in rating_list:
        print(ratings.name)
    return render(request, 'Home/home.html', {
        'rating_list': rating_list
    })


def search_chanel(request):
    if request.method == 'POST':
        search = request.POST['search']
        searched = rating.objects.filter(name__contains=search)
        p = Paginator(rating.objects.filter(name__contains=search), 2)
        page = request.GET.get('page')
        chanels = p.get_page(page)
        return render(request, 'Home/search_chanel.html',
                      {'search': search,
                       'results': searched,
                       'chanels': chanels})
    if request.method == 'GET':
        p = Paginator(rating.objects.filter(name__contains=search), 2)
        page = request.GET.get('page')
        chanels = p.get_page(page)
        return render(request, 'Home/search_chanel.html',
                      {'search': search,
                       'results': searched,
                       'chanels': chanels})
