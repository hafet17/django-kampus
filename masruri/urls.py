from django.urls import path
from . controllers import dashboard, auth, custumer, product, order

urlpatterns = [
    path('', dashboard.home, name='home'),
    path('products/', product.index, name='products'),
    path('create_product/', product.createProducts, name='create_product'),
    path('update_product/<str:pk>', product.updateProducts, name='update_product'),
    path('delete_product/<str:pk>', product.deleteProducts, name='delete_product'),
    path('custumer/<str:pk>', custumer.index, name='custumer'),
    path('account/', custumer.accountSetting, name='accountpage'),
    path('create_order/', order.createOrder, name='create_order'),
    path('update_order/<str:pk>', order.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', order.deleteOrder, name='delete_order'),
    path('register/', auth.registerPage, name='register'),
    path('login/', auth.loginPage, name='login'),
    path('logout/', auth.logoutPage, name='logout'),
    path('user/', auth.userPage, name='user-page'),
]
