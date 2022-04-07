from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedBack


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


def add_review(request):
    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Ваш запрос отправлен'))
        return redirect('review')
    else:
        form = FeedBack()
    return render(request, 'feedback/review.html', {'form': form})

