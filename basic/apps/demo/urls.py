from django.urls import path

from .api import animals
from .views import ClassBasedView, GenericClassBasedView, function_based_view, integrated_vue_view

urlpatterns = [
    path('', GenericClassBasedView.as_view(), name='main'),
    path('cbv', ClassBasedView.as_view(), {'template': 'main.html'}, name='main'),
    path('fbv', function_based_view, name='main'),
    path('api/animals/', animals, name='animals'),
]
