from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results,name='search_results'),
    url(r'^user/', views.profile, name='profile'),
]