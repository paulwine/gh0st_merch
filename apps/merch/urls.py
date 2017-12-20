from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^log_reg$', views.log_reg),
    url(r'^main$', views.main),
    url(r'^logprocess$', views.logprocess),
    url(r'^regprocess$', views.regprocess),
    url(r'^logout$', views.logout)
]