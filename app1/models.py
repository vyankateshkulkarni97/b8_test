from django.db import models

# Create your models here.
# ORM -- object Relational Mapper py 61:- 17
# class ActiveEmployee(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_active=True) # model.objects.all
# # define class create
# class InActiveEmployee(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(inactive=False)

class Employee(models.Model): # Table
    # default .id
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length = 200)
    email = models.EmailField(null=True)
    date_joined = models.DateField(auto_now=True , null=True)
    Joine = models.BooleanField(default=True)
    # date_updated = models.DateTimeField(auto_now_add=True , null=True)
    is_active=models.BooleanField(default=True)
    # activeemp = ActiveEmployee()
    # inactiveemp = InActiveEmployee()
    # all_data = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employee"

class EmployeeForm(models.Model): # django create form
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length = 200)
    email = models.EmailField(null=True)
    Joine = models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "form"


        
    def show_details(self):
        print(f"""---------------------------------------------------
Employee Name:-{self.name}
Employee Age:-{self.age}
Employee Mobile:-{self.mobile_num}
Employee Address:-{self.address}""")

    @classmethod
    def get_data_above_age(cls):
        return cls.objects.filter(age__gte=25) # gt gte lt lte ,startswith , endswith

    @classmethod
    def gvt_avg_age(cls):
        '''average age of all person'''
        data = Employee.objects.all().values("id","name","age")        
        lst = list(map(lambda x : x['age'],list(data)))
        return sum(lst)//len(lst)

    @classmethod
    def get_active_data(cls):
        return cls.objects.filter(is_active=True)

    # in active data
    @classmethod
    def get_inactive_data(cls):
        return cls.objects.filter(inactive=False)


# class User(models.Model): # 63
#     first_name =
#     email_id = 
#     is_active = 

class CommonClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        abstract = True

class College(CommonClass):
    adr = models.CharField(max_length=500)
    est_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "college"

class Principal(CommonClass):
    exp = models.FloatField()
    qual =models.CharField(max_length=50)
    college = models.OneToOneField(College , on_delete=models.CASCADE , related_name="princi")
    class Meta:
        db_table = "principal"

class Department(CommonClass): # small letters
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete =models.CASCADE, related_name="depts")
    class Meta:
        db_table = "dept"
        # unique_together = (("name" , "college"),)

class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete = models.CASCADE, related_name="studs")
    class Meta:
        db_table = "student"

class Subject(CommonClass):
    is_pratical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student)
    dept = models.ForeignKey(Department ,on_delete=models.CASCADE, related_name="subjs")
    class Meta:
        db_table ="subject"


# get models from database 
# ERD -- Entity Relationship Diagram


    