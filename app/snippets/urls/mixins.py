from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..apis import mixins

urlpatterns = [
    path('', mixins.SnippetList.as_view()),
    path('<int:pk>/', mixins.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
