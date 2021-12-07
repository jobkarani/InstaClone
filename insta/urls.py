from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('search/', views.search_results,name='search_results'),
    path('user/', views.profile, name='profile'),
    path('comments/<image_id>', views.comments,name='comments'),
]