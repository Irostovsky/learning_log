"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^stores/$', login_required(views.StoreListView.as_view()), name='store_list'),
    url(r'^load_keys$', login_required(views.LoadKeysView.as_view()), name='load_keys'),
]
