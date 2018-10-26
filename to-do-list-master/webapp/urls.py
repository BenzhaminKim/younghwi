from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webapp-home'),
    path('note',views.note, name='webapp-note'),
    path('about',views.about, name='webapp-about')
]
