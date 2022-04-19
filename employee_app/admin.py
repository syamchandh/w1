from atexit import register
from django.contrib import admin
from employee_app.models import productdetails

admin.site.register(productdetails)
