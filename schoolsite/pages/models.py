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
# below are commands for migrations 
# python manage.py makemigrations
# python manage.py migrate  
#  python manage.py showmigrations                 
                                                                                  