from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^log_reg$', views.log_reg),
    url(r'^main$', views.main),
    url(r'^logprocess$', views.logprocess),
    url(r'^regprocess$', views.regprocess),
    url(r'^purchase/(?P<image_id>\d+)$', views.purchase),
    url(r'^addtocart/(?P<image_id>\d+)$', views.addtocart),
    url(r'^shoppingcart/(?P<user_id>\d+)$', views.shoppingcart),
    url(r'^logout$', views.logout)
]