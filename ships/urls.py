from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("characters-<int:character_id>", views.characters, name='character')
]