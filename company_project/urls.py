"""company_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hr_page/', views.home , name="home_page"),
    path('employee/', views.show_employee , name="employee"), # show employees
    path('update/<int:pk>/', views.update_employee , name="update_employee"),
    path('delete/<int:pk>/', views.delete_employee , name="delete_employee"),
    path('soft-delete/<int:pk>/', views.soft_delete_employee , name="soft_delete_employee"),
    path('inactive_employess/', views.show_inactive_employess , name="show_inactive_employess"),
    path('registration/', views.Emp , name="New_employee"),



    # path('inactive-employee/', views.show_inactive_employess , name="show_inactive_employess"),
    
    # User url
    path('employee_form/', views.employee_form , name="employee_form"),
    path('employee_login/', views.employee_login , name="employee_login"),
    path('logout/',views.logout_user , name="logout_user"),


    # User url
    # path('register/',user_views.register_request , name="register"),
    # path('login/',user_views.login_request , name="login_user"),

]
