# from django import forms
# from .models import Employee

# class EmployeeForm(forms.ModelForm): # django create form
#     class Meta:
#         model = Employee
#         fields =  ('__all__')
#         exclude = ("is_active",)

# class EmployeeLogin(forms.Form): # user create form
#     Email = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Email'}))
#     Password = forms.CharField(widget = forms.PasswordInput())



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployeeForm(UserCreationForm):
    email = forms.EmailField(required=True)
    frist_name = forms.CharField(max_length = 100 , required=True)
    last_name = forms.CharField(max_length = 100 , required=True)


    class meta:
        model = User
        fields = ("firs_name", "last_name","username","email","password","password2")

    def save(self , commit = True): # over-ridden save method from UserCreation
        user =  super(EmployeeForm , self).save(commit = False)
        # print(user. __dict__)
        user.email = self.cleaned_data['email']
        user.frist_name = self.cleaned_data['frist_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
