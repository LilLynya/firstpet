from django.urls import path

from dio.views import *

app_name = 'dio'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('info/', about_us, name='about_us'),
]
