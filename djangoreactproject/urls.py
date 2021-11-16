from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from customers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/customers/', views.customers_list),
    url('api/customers/(?P<pk>[0-9]+)', views.customers_detail),
]
