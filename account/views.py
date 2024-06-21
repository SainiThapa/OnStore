from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

from django.contrib.auth.decorators import user_passes_test

from .validate_register import loginform, registerform, unauthenticated_user

def user_required(user):
    return user.is_authenticated


# Create your views here.
class Auth:
    @unauthenticated_user
    def sign_up(request):
        if request.method=="POST":
            user=registerform(request)
            if not user:
                raise ValueError("Error creating user")
            else:
                return redirect('/account/login')
        return render(request,"account/signup.html")

    @unauthenticated_user
    def login(request):
        if request.method=="POST":
            user=loginform(request)
            if not user:
                raise NameError("Error logging in the user")
            else:
                auth.login(request,user)
                return redirect("/")
        return render(request,"account/login.html")
    
    @user_passes_test(user_required)
    def logout(request):
        auth.logout(request)
        return redirect("/")