from django.urls import path, include

from credentials import views

urlpatterns = [


    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('demo', views.demo, name='demo'),
]