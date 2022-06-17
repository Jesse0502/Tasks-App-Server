from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("todo", views.single_todo, name="get_single_todo"),
    path("add", views.add_todo, name="add_todo"),
    path("update", views.update_todo, name="update_todo"),
    path("delete", views.delete_todo, name="delete_todo"),
]
