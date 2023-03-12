from django.contrib import admin
# from .models import Employee
from .models import *

# Register your models here.
# admin.site.register(Employee)

admin.site.register([Employee , College , Principal , Department , Student , Subject ])