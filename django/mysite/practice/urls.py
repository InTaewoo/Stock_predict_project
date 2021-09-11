from django.urls import path
from . import views

appname = 'practice'

urlpatterns = [
    path('', views.index, name='index'),

]