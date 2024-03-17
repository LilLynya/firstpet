from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from workspace.views import *

app_name = 'workspace'

urlpatterns = [
    path('work/', workspace, name='workspace'),
    path('addgroup/', add_group, name='add_group'),
    path('creategroup/', create_group, name='create_group'),
    path('mygroup/', my_group, name='my_group'),
    path('profile/<str:user_id>', user_profile, name='user_profile'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('task/', make_task, name='make_task'),
]
