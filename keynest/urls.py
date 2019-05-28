"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.IndexView.as_view(), name='index'),
]
