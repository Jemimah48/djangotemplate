from django.urls import path
from jemimahapp import views
urlpatterns = [
    path('', views.index, name='index'),


]