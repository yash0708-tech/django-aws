from django.contrib import admin

# Register your models here.
from .models import Standard, Student

admin.site.register(Standard)
admin.site.register(Student)
