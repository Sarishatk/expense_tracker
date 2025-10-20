from django import forms
from User.models import User

class UserRegistrationForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username','first_name','last_name','email','password']

    # username = forms.CharField(max_length=50)

    # first_name = forms.CharField(max_length=50)

    # last_name = forms.CharField(max_length=50)

    # email = forms.EmailField()

    # password = forms.CharField(max_length=50)