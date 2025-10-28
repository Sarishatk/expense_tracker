from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from expense_app.forms import ExpenseForm
from expense_app.models import Expense

class Add_Expense_view(View):

    def get(self, request):

        form = ExpenseForm()

        return render(request,"expense_add.html",{'form':form})
     
    def post(post,request):

        print(request.POST)

        form = ExpenseForm(request.POST)

        if form.is_valid():

            print(form.cleaned_data)

            expense = form.save(commit= False)

            expense.user = request.user

            expense.save()

        return render(request,"expense_add.html",{'form':form})


class ExpenseListView(View):

    def get(self,request):

        expenses = Expense.objects.filter(user = request.user)

        return render(request,"expense_list.html",{'expenses':expenses})
                                            
