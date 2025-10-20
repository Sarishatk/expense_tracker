from django.shortcuts import render
from django.views.generic import View

from User.froms import UserRegistrationForm
# Create your views here.

# view : registrationView

# methods required : get , post

class RegisterView(View):

    def get(self,request):

        form = UserRegistrationForm()

        return render (request,"signin.html",{'form':form})


