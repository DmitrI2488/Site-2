from django.shortcuts import render, get_object_or_404

from Home.models import rating, Comment

from django.core.paginator import Paginator
from .forms import CommentForm
import sqlite3

# def add_feedback(request):
#     if request.method == 'POST':
#         form = FeedBack(request.POST)
#         if form.is_valid():
#             form.save()
#         messages.success(request, ('Ваше сообщение отправлено'))
#         return redirect('feedback')
#     else:
#         form = FeedBack()
#     return render(request, 'feedback/feedback.html', {'form': form})


def show_chanel(request, chanel_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            chanelss = request.GET.get('pk')
            name = form.cleaned_data
            names = name['name']
            body = name['body']
            print(names, body, chanelss)
            # conn = sqlite3.connect("db.sqlite3")
            # cursor = conn.cursor()
            # cursor.execute(f"INSERT INTO Home_comment VALUES ('{chanelss}','{names}','{body}')")
            # conn.commit()
            # cursor.close()
            # conn.close()
            # comments = Comment.objects.get(pk=1)
            # s = Comment.objects.create(chanel_id=chanelss, name=name, body=body)
            # comments.chanel.add(s)
            b = Comment(chanel_id=chanelss, name=names, body=body)
            Comment.save()
    else:
        chanel = rating.objects.get(pk=chanel_id)
        form = CommentForm()
        return render(request, 'Home/show_chanel.html', {
            'chanel': chanel,
            'form': form,
        })


def all_events(request):
    rating_list = rating.objects.all()
    # for ratings in rating_list:
    #     print(ratings.name)
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
        print(pk)
        searched = rating.objects.filter(name__contains=pk)
        p = Paginator(rating.objects.filter(name__contains=pk), 2)
        page = request.GET.get('page')
        chanels = p.get_page(page)
        return render(request, 'Home/search_chanel.html',
               {'search': pk,
                'results': searched,
                'chanels': chanels})
