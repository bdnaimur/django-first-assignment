from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.new_one),
]
