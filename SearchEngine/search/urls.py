from django.conf.urls import url
from search import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^searchmeth/$', views.searchmeth, name='searchmeth'),
]
