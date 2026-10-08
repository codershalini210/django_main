from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description =models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    no_of_pages = models.IntegerField(default=0)
    def __str__(self):
        return str(self.title)
class Student(models.Model):
    name = models.CharField(max_length=50)
    age= models.IntegerField(default = 5 )
    email= models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    isregular =  models.BooleanField(default=True)
    def __str__(self):
        return str(self.name)

class Department(models.Model):
    name = models.CharField(max_length = 80)
    description = models.CharField(max_length = 150)
    def __str__(self):
        return str(self.name)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    salary = models.FloatField()
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name="employees")
    def __str__(self):
        return str(self.name)
# below are commands for migrations 
# python manage.py makemigrations
# python manage.py migrate  
#  python manage.py showmigrations                 
                                                                                  