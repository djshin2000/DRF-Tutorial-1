from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import apis

app_name = 'members'
urlpatterns = [
    path('', apis.UserList.as_view(), name='user-list'),
    path('<int:pk>/', apis.UserDetail.as_view(), name='user-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
