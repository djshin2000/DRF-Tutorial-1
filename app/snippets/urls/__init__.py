from django.urls import path, include


app_name = 'snippets'
urlpatterns = [
    path('api-view/', include('snippets.urls.api_view')),
    path('mixins/', include('snippets.urls.mixins')),
    path('generic/', include('snippets.urls.generic')),
    path('viewsets/', include('snippets.urls.viewsets')),
    path('routers/', include('snippets.urls.routers')),
]
