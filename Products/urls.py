from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('contact',views.contactus,name="contactus"),
    path('products',views.products,name="products"),
    path('categories',views.categories,name="categories"),
    path('mycart',views.cart,name="cart"),

]