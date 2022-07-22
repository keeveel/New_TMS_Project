from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index_page', views.index_page, name='index_page'),
    path('about', views.about, name='about'),
    path('login', views.login_page, name='login_page')
]