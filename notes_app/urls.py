from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'note_app'

urlpatterns = [
    #path('' ,  views.all_notes, name='all_notes'),
    url(r'^$', views.all_notes, name='all_notes'),
    #path('<int:id>/', views.detail, name='note_detail'),
    url(r'^(?P<id>\d+)$',views.detail,name='note_detail'),
    #path('<str:slug>/' ,views.detail,name='note_detail'),
    url(r'^(?P<slug>[-\w]+)?$',views.detail,name='note_detail'),
    #path('add/',views.note_add,name='add_note'),
    url(r'^add/$',views.note_add,name='add_note'),
    #path('<str:slug>/' ,views.edit,name='note_edit'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='note_edit'),

]