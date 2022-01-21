from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('', cache_page(60)(views.HomepageView.as_view()), name='home'),
    path('hellohumans', views.HellohumanspageView.as_view(), name='hellohumans'),
    path('hello/<int:person_id>', views.HellopageView.as_view(), name='hello')
]

