from django.urls import include, path

from . import views

urlpatterns = [
    path("contact/", views.contact),
    path("about/", views.about),
]
