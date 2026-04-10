from django.contrib import admin

# Register your models here.
from app1.models import employee
class employee_admin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','emp_salary']
admin.site.register(employee,employee_admin)