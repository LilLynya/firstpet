from django.urls import path

# Views
from .views import AuthView, signup_page

app_name = 'users'

urlpatterns = [
    path('login/', AuthView.as_view(), name='login'),
    path('signup/', signup_page, name='singup'),
]
