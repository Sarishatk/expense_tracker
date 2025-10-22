from django.shortcuts import render
from django.views.generic import View
from User.models import User

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

        return render(request,"signin.html",{'form':form})


