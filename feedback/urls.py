from django.urls import path
from . import views


urlpatterns = [
    path('feedback/', views.add_feedback, name='feedback'),
    path('review/', views.add_feedback, name='review'),
]