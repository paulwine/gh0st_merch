from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^main$', views.main),
    url(r'^logprocess$', views.logprocess),
    url(r'^regprocess$', views.regprocess),
    url(r'^logout$', views.logout)
]