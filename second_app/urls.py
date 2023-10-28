from django.urls import include, path

from . import views

urlpatterns = [
    path("courses/", views.courses),
    path("feedback/", views.feedback),
]
