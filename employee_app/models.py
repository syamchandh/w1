
from django.db import models

# Create your models here.
class productdetails(models.Model):
    employee_name=models.CharField(max_length=255)
    qualification=models.TextField(default=False)
    dob=models.DateField()
    designation=models.TextField() 
    address=models.TextField(max_length=255)
    mobile=models.IntegerField()
    emaill=models.TextField()

    def __str__(self):
        return self.employee_name
    

    

