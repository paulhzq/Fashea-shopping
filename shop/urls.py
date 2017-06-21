from django.conf.urls import url,include
from . import views
from django.contrib.auth import login,logout

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^login/',login,name="login"),
    url(r'^logout/$',logout, {'next_page': '/'}, name="logout"),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]
