from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('custumer/<str:pk>', views.custumer, name='custumer'),
    path('student/', views.student, name='student'),
]
