from django.db import models

# Create your models here.
class employee(models.Model):
    emp_name=models.CharField(max_length=15)
    emp_id=models.IntegerField(unique=True)
    emp_salary=models.FloatField()
    