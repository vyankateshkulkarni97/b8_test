from app1.models import *
from django.contrib.auth.models import User
import sqlite3

# to get all data
# obj = Employee.objects.all()
# print(list(obj))


# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())
# for i in obj:
#     print(Employee.__dict__)

# to get first Employee
# first_r =Employee.objects.first()
# print(first_r)

# to get record by id
# try:
#     obj = Employee.objects.get(id=10)
#     print(obj)
# except Employee.DoesNotExist:
#     print("Record dose not exits..")

# to get multiple record by passing filename

# Employee.objects.get(age=23)

# obj = Employee.objects.filter(age=23)
# print(obj)
# print(obj.query)

# modifiy existing data
# p1 = Employee.objects.get(id=1)
# print(p1.__dict__)
# p1.mobile_num = 9892648457
# print(p1.__dict__)
# p1.save()
# p1.delete

# create objects:-
# p1 = Employee(name="jay", age=21 , mobile_num=956458454 , address="Nashik")
# p1.save()

# 2nd way to save data
# Employee.objects.create(name="sanket" , age=31 , mobile_num=764845155 , address="ambajogai")


# bulk_create
# p1 = Employee(name="akash", age=22 , mobile_num=8568845154 , address="mumbai")
# p2 = Employee(name="chandu", age=31 , mobile_num=956122354 , address="thane")
# p3 = Employee(name="saurabh", age=35 , mobile_num=924558454 , address="nagar")
# p4 = Employee(name="akshya", age=33 , mobile_num=980000454 , address="amravti")

# Employee.objects.bulk_create([p1,p2,p3,p4])

# count:-
# print(Employee.objects.count())

# delete all record
# Employee.objects.all().delete()

# to delete multiple records
# Employee.objects.filter(age=35).delete()

# startwith 
# p1 = Employee.objects.filter(name__startswith="A")
# print(p1) 

# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())

# print(Employee.objects.filter(name__endswith="A")) 

#
# print(Employee.objects.exclude(name__startswith="A"))

# exists and orderpy
# print(Employee.objects.filter(id=1).exists())

# print(Employee.objects.filter(name="Ajay").exists())

# orderby:-
# print(Employee.objects.all().order_by("-id")) # id - asc , -id:- dsec
# print(Employee.objects.all().order_by("name"))

# Employee.objects.get(id=1).show_details()

# for Emp_obj in Employee.objects.all():
#     Emp_obj.show_details()

# print(Employee.get_data_above_age())

# contians
# print(Employee.objects.filter(name__contains="A"))

# data = Employee.objects.all().values("id","name","age")
# print(data)
# for i in data:
#     print(i)

# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())
# print(list(data))

# print(list(map(lambda x : x['age'],list(data))))

# lst = list(map(lambda x : x['age'],list(data)))
# print(sum(lst)//len(lst))

# data = Employee.objects.all().values_list("name")
# print(list(data))


# User.objects.create_superuser(username="pallavi" , password="Vyankatesh@97")

# print(Employee.objects.all())

# delete - soft delete and hard delete
# data = Employee.objects.filter(id__in=[3 , 5]).update(is_active=False)
# print(data)



# p1 = Employee.objects.get(id=3)
# p1.mobile_num = 88
# p1.is_active = False
# p1.save() 


# is active data
# print(Employee.objects.filter(is_active=True))

# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())

# is active data showing
# print(Employee.activeemp.all())

# is inactive data showing
# print(Employee.inactiveemp.all()) # 64

# print(Employee.all_data.all())

# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())
# clgs = College.objects.all()
# princ =Principal.objects.all()
# depts = Department.objects.all()
# stud = Student.objects.all()
# subj = Subject.objects.all()

# print(clgs , princ ,depts , stud, subj)

# for depts in depts:
#     print(depts.__dict__)

# 
# for stud in stud:
    # print(stud.__dict__)


# for subj in subj:
    # print(subj.__dict__)

# college get principal fetch
# clg = clgs[0] # D Y Patile
# print(clg.principal)  # Vyankatesh

# principal to college fetch
# Vyankatesh_obj = Principal.objects.first()
# print(Vyankatesh_obj.college)  # D Y Patile

# college to department
# print(clg.department_set.all())

# department to college
# dept = Department.objects.first()
# print(dept.college)

# department to subjects
# dept = Department.objects.first()
# print(dept.student_set.all())

# 
# all_depts = Department.objects.all()
# for dept in all_depts:
#     print(f"Department Name:- {dept.name} , Studs:- {list(dept.student_set.all())}")

#
# all_depts = Department.objects.all()
# d = {}
# for dept in all_depts:
#     print(f"Department Name:- {dept.name} , Studs:- {list(dept.student_set.all())}")
#     print(f"Department Name:- {dept.name} , Studs:- {list(dept.student_set.all())}")
#     d[dept.name] = list(dept.student_set.all())
# print(d)

#
# s1 = Student.objects.first()
# print(s1.dept)

#
# s1 = Student.objects.get(id=8)
# print(s1.dept)

#
# studs = Student.objects.all()
# for stud in studs:
#     print(stud)

#
# studs = Student.objects.all()
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept  #stud.dept.name
# print(stud_dept_dict)

#
# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())

# clg = College.objects.get(id=1)
# print(clg.princi)
# print(clg.depts.all())

# dept = Department.objects.get(id=1)
# print(dept)
# print(dept.subjs.all())

# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subjs.all())

# print( [dept.subjs.all() for dept in Department.objects.all()])

# 
# print( [list(dept.subjs.all()) for dept in Department.objects.all()])

# college to student:-
# clg = College.objects.get(id=1)
# print(clg.depts.all()[1].studs.all())

# print(clg.depts.all()[0].studs.all())

# print(clg.depts.all()[2].studs.all())

# for dept in clg.depts.all():
#     print(dept.studs.all())
# studs_list =[]
# for dept in clg.depts.all():
#     studs_list.extend(dept.studs.all())
# print(studs_list)

# s1 = Student.objects.get(id=1)
# print(s1)

# student to college get in revers directions
# s1 = Student.objects.get(id=1)
# print(s1.dept.college)

# college.objects.create(name="MIT", adr ="Kothrud")
#
# c1 = College.objects.get(id=1) 
#
# p1 = Principal(name="abc" , exp=20 , qual="PHD" , college=c1) as it is pass objects of college
# p1.save()

# p1 = Principal(name="abc" , exp=20 , qual="PHD" , college_id=c1) 
# p1.save()

# Department.objects.create(name="Production" , dept_str=80 , college=c1)

# Student.objects.create(name="A", marks=44, age=18 )
# Student.objects.create(name="B", marks=75, age=31)
# Student.objects.create(name="C", marks=84, age=26)

# s1 , s2 , s3 = Student.objects.filter(id__gt=9)
# print(s1)

# prod_dept = Department.objects.get(id=4))
# print(dir(prod_dept.studs))

# prod_dept.studs.add(s2 , s3) # one to many -- add students in departments

# print(dir(prod_dept.studs))

# college -- mit -- id -3
# department -- production id -4
# student - A-10 , B-11 , C-12

# select_related:-

# studs = Student.objects.all()[0:5]
# print(studs.dept)

# studs = Student.objects.all()
# studs = Student.objects.select_related("dept")
# for stud in studs:
#     print(stud.dept) # 67

# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())

# first way
# from django.db import connection
# cursor = connection.cursor()
# cursor.execute(''' SELECT * FROM student ''')
# data = cursor.fetchall()

# print(data)
# data = cursor.fetchmany(3)
# print(data)

# second way
# data = Student.objects.raw(''' SELECT * FROM student ''')
# for i in data:
#     print(i)

# multiple Database
#MySQL , SQLite
# conn = sqlite3.connect('second_db')
# print("Opened database successfully",conn)

# DATABASE = "second_db"
# data = Student.objects.using(DATABASE).all()
# print(data)

# data = Student.objects.using(DATABASE).create()

# c1 = College.objects.using("second_db").create(name="MIT" , adr="Pune")
# d1 = Department.objects.using("second_db").create(name="Entc" , dept_str=60 , college=c1)
# s1 = Student.objects.using("second_db").create(name="Akash",marks=78 , age=25 , dept=d1)
# s1 = Student.objects.using("second_db").create(name="Suyog",marks=87 , age=24 , dept=d1)
# subj1 = Subject.objects.using("second_db").create(name="Data signal",is_pratical=True ,  dept=d1)


# exec(open(r'D:\python program\b9_django\company_project\app1\all_operation.py').read())
# studs = Student.objects.using(DATABASE).all()
# print(studs)