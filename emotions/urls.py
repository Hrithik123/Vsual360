from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('vsual2.html', views.index2, name='index2'),
    path('vsual3.html', views.index3, name='index3')
]