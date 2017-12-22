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
    url(r'^checkout/(?P<cart_id>\d+)$', views.checkout),
    url(r'^payment/(?P<cart_id>\d+)$', views.payment),
    url(r'^thank_you$', views.thank_you),
    url(r'^clear_cart/(?P<cart_id>\d+)$', views.clear_cart),
    url(r'^logout$', views.logout)
]