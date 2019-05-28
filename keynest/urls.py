"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^load_keys$', views.LoadKeysView.as_view(), name='load_keys'),
]
