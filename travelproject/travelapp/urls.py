
from django.urls import path, include

from travelapp import views

urlpatterns = [


    path('',views.demo1,name='demo1'),
]