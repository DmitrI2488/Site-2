from django.urls import path
from . import views

urlpatterns = [
    path('rating', views.ratings, name='rating'),
    path('failed', views.failed, name='failed')
]
