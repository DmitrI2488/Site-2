from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='home'),
    path('chanel/<chanel_id>', views.show_chanel, name="page"),
    path('search_chanel', views.search_chanel, name='search')
]
