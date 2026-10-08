from django.contrib import admin
from .models import Book
from .models import Student
from .models import Department,Employee
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Employee)
# Register your models here.
