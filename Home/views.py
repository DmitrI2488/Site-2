from django.shortcuts import render, get_object_or_404

from Home.models import rating

from django.core.paginator import Paginator
from .forms import CommentForm

def add_feedback(request):
    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Ваше сообщение отправлено'))
        return redirect('feedback')
    else:
        form = FeedBack()
    return render(request, 'feedback/feedback.html', {'form': form})


def show_chanel(request, chanel_id):
    ratings = get_object_or_404(rating, pk=chanel_id)
    print(ratings)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.chanel = ratings
            comment.save()
    else:
        chanel = rating.objects.get(pk=chanel_id)
        form = CommentForm
        return render(request, 'Home/show_chanel.html', {
            'chanel': chanel,
            'form': form,
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
    else:
        pk = request.GET.get('pk')
        searched = rating.objects.filter(name__contains=pk)
        p = Paginator(rating.objects.filter(name__contains=pk), 2)
        page = request.GET.get('page')
        chanels = p.get_page(page)
        return render(request, 'Home/search_chanel.html',
               {'search': pk,
                'results': searched,
                'chanels': chanels})
