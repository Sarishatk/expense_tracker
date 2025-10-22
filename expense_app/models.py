from django.db import models

# Create your models here.
class Expense(models.Model):

    category_choice = [
        ('food','Food'),
        ('')
    ]