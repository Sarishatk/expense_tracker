from django.shortcuts import render,redirect
from django.views.generic import View
from User.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

from User.froms import UserRegistrationForm
# Create your views here.

# view : registrationView

# methods required : get , post

class RegisterView(View):

    def get(self,request):

        form = UserRegistrationForm()

        return render (request,"signin.html",{'form':form})
    
    def post(self,request):

        print(request.POST)

        username = request.POST.get("username")

        first_name =  request.POST.get("first_name")

        last_name =  request.POST.get("last_name")

        password = request.POST.get("password")

        email =  request.POST.get("email")

        User.objects.create_user(username =username,first_name = first_name, last_name = last_name,password=password,email=email )

        form = UserRegistrationForm()

        return redirect('signin')


class LoginView(View):

    def get(self,request):

        return render(request,"login.html")
    
    def post(self,request):

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)

        if user:

            login(request,user)

            return redirect("signin")
        
        return redirect("login")
    
class logOut(View):

    def get(self,request):

        logout(request)

        return redirect("login")


