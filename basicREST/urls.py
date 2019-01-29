from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('users/', views.index, name="users"),
    path('usersget/', views.get, name="usersget"),
    path('userspost/', views.post, name="userspost"),
    path('usersput/', views.put, name="usersput"),
    path('usersdelete/', views.delete, name="usersdelete"),
]