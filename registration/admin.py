from django.contrib import admin
from .models import Student, Staff, Guest, Laptop

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Guest)
admin.site.register(Laptop)

