from django.shortcuts import render

# Create your views here.
class Auth:
    def sign_up(request):
        return render(request,"account/signup.html")
    
    def login(request):
        return render(request,"account/login.html")