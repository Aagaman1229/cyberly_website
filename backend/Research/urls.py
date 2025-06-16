from django.urls import path
from .views import research_list

urlpatterns = [
    path('research/', research_list, name='research_list'),
]
