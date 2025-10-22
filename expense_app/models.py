from django.db import models
from django.contrib.auth import User

# Create your models here.
class Expense(models.Model):

    category_choice = [
        ('food','Food'),
        ('Travel','Travel'),
        ('shopping','shopping'),
        ('Rent','Rent'),
        ('Other','Other')
    ]

    category = models.CharField(max_length=20,choices=category_choice)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    amount = models.DecimalField(max_digits=10,decimal_places=2)

    payment_date = models.DateField()

    created_date = models.DateField(auto_now_add=True)
    # payment date manually add chythu kodkkanam
    

