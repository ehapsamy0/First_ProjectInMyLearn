from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    #path('' ,  views.allnotes, name='all_notes'),
    url(r'^$', views.allnotes, name='all_notes'),

]