from django.urls import path
from django.conf.urls import url
from . import views
#from Restaurant.views import request_page
from django.urls import path,include

app_name = 'Restaurant'

urlpatterns = [
 #   path('', views.customer_list, name='customer_list'),
     path('', views.index, name='index'),
#    path('', views.request_page(request="POST"), name='reuest_page'),
   # path('create-new-product/', views.create_new_product, name='create_new_product')
     #path('<int:pk>//', views.request_page, name='favorite_item'),
    #path('request_page/', include('Restaurant.urls')),
     url(r'detail/$',views.detail1 ,name='detail1'),
]