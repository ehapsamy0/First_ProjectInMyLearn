from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView




app_name = 'accounts'

urlpatterns = [
    #path('' ,  views.home, name='home'),
    url(r'^$', views.home, name='home'),
    #path('login/',LoginView.as_view(template_name='login.html')),
    url(r'^login/$',LoginView.as_view(template_name='login.html'),name='login'),
    #path('logout/',LogoutView.as_view(next_page='/',,,,,,,template_name='login.html'), name='logout'),
    url(r'^logout/$', LogoutView.as_view(next_page='/notes'),name='logout'),
    #path('sigup/', views.register ,name='register'),
    url(r'^sigup/$', views.register ,name='register'),
    #path('<str:slug>/' ,views.profile,name='profile'),
    url(r'^(?P<slug>[-\w]+)/$',views.profile,name='profile'),
    #path('<str:slug>/edit' ,views.edit_profile(),name='edit_profile'),
    url(r'^(?P<slug>[-\w]+)/edit$',views.edit_profile,name='edit_profile'),
    #path('<str:slug>/change_password' ,views.change_password, name='change_password'),
    url(r'^(?P<slug>[-\w]+)/change_password', views.change_password, name='change_password'),


]