from django.urls import path 
from . import views #import views module from current directory

urlpatterns = [
    path('', views.index, name='index'), 
    path('brian/', views.brian, name='brian'),
    path('david/', views.david, name="david"),
    path("<str:name>/", views.greet, name="greet"),#maps the root URL to the index view
]