from django.shortcuts import render

# Create your views here.
class Register:
    def sign_up(request):
        return render(request,"account/signup.html")