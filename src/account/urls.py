from django.urls import path
from .views import Register

urlpatterns=[
    path('register',Register.sign_up,name="sign_up"),
]