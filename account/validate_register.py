from functools import wraps
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect

from account.models import Client

def registerform(request):
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        phone=request.POST.get("phone")
        address=request.POST.get("address")

        password=request.POST.get("password1")
        conf_password=request.POST.get("password2")
        
        user=None

        try:
            user1=User.objects.filter(username=username, email=email)
            raise Exception("User already exists")
        except:
            if email is not None and username is not None and phone is not None and address is not None and password==conf_password:
                user=User.objects.create_user(username=username, password=password, email=email)     
                user.save()
                client=Client.objects.create(user=user,phone=phone,address=address,interactions=0)
                client.save()
        return user
    
def unauthenticated_user(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request,"You need to logout first")
            return redirect('/')  # Redirect authenticated users
        return view_func(request, *args, **kwargs)
    return wrapper

def loginform(request):
    email =  request.POST.get("email")
    password = request.POST.get("password")
    if email is not None and password is not None:
        user=User.objects.get(email=email)
        if user.check_password(password):
            print("User exists")
            return user
    else:
        raise ValueError("User doesn't exist")