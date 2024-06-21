from django.urls import path
from .views import Auth

urlpatterns=[
    path('register',Auth.sign_up,name="sign_up"),
    path('login',Auth.login,name="login"),
    path('logout',Auth.logout,name="logout"),

]