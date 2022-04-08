from django.shortcuts import render

from Home.models import rating


def all_events(request):
    rating_list = rating.objects.all()
    for ratings in rating_list:
        print(ratings.name)
    return render(request, 'Home/home.html', {
        'rating_list': rating_list
    })
