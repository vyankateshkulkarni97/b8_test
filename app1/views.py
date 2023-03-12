from django.shortcuts import render , HttpResponse, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required

from django.shortcuts import render , redirect
from .forms import EmployeeForm
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.forms import AuthenticationForm

@login_required
def home(request):
    if request.method == "POST":
        # print(request.POST)
        Eid = request.POST.get("Employee_id")
        name = request.POST.get("Employee_name")
        age = request.POST.get("Employee_age")
        mobile_num = request.POST.get("Employee_num")
        address = request.POST.get("Employee_address")
        email = request.POST.get("Employee_email")
        date_join = request.POST.get("Employee_join")
        joine = request.POST.get("Employee_joine")
        # print(name , age , mobile_num , address , email , date_join)
        if  joine == "Yes":
            joine=True
        else:
            joine=False
            
        if not Eid:
            Employee.objects.create(name=name , age=age , mobile_num=mobile_num, address=address, email=email , date_joined=date_join , Joine=joine)
        else:
            employee_obj = Employee.objects.get(id=Eid)
            employee_obj.name = name
            employee_obj.age = age
            employee_obj.mobile_num = mobile_num
            employee_obj.address = address
            employee_obj.email = email
            employee_obj.date_joined = date_join 
            employee_obj.Joine = joine
            employee_obj.save()
        return redirect("home_page")  #return render(request , "Hr_page.html")
    elif request.method == "GET":
        return render(request , "Hr_page.html" )

@login_required
def show_employee(request):
    return render (request , "show_employee.html" , {"employee":Employee.objects.filter(is_active=True)})
@login_required
def update_employee(request, pk): # pk = id
    employee_obj = Employee.objects.get(id=pk)
    # print(employee_obj)
    return render (request , "Hr_page.html" , context={"one_employee":employee_obj})
@login_required
def delete_employee(request, pk): # pk = id
    Employee.objects.get(id=pk).delete()
    return redirect("employee")

@login_required
def soft_delete_employee(request, pk): # pk = id
    employee_obj = Employee.objects.get(id=pk) # pk = id
    employee_obj.is_active = False
    employee_obj.save()
    return redirect("show_inactive_employess")
@login_required
def show_inactive_employess(request):
    return render (request , "show_employee.html" , {"employee":Employee.objects.filter(is_active=False), "inactive": True})


# from django.shortcuts import render , redirect
# from .forms import EmployeeForm
# from django.contrib.auth import login , authenticate , logout
# from django.contrib.auth.forms import AuthenticationForm


def employee_form(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("employee_login")
    form = EmployeeForm()
    return render (request=request , template_name="employee_form.html" , context={"register_form":form})


def employee_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request , user)
                return redirect("home_page")
            else:
                return redirect("employee_login")
        else:
            return redirect("employee_login")
    form = AuthenticationForm()
    return render(request=request , template_name="employee_login.html",context={"login_form":form})

def logout_user(request):
    logout(request)
    return redirect("employee_login") 



def Emp(request):
    if request.method == "POST":
        name = request.POST.get("Employee_name")
        age = request.POST.get("Employee_age")
        mobile_num = request.POST.get("Employee_num")
        address = request.POST.get("Employee_address")
        email = request.POST.get("Employee_email")            
        Employee.objects.create(name=name , age=age , mobile_num=mobile_num, address=address, email=email )
    return render(request , "registration.html")
   