from django.contrib import admin
from .models import Courses,Professors,CourseReview,ProfReview,Prof_to_subj,ProfRating,CourseRating,Complaints,Employee,Liker
# Register your models here.

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'




# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)







admin.site.register(Courses)
admin.site.register(Professors)

admin.site.register(CourseReview)
admin.site.register(ProfReview)
admin.site.register(Prof_to_subj)
admin.site.register(CourseRating)
admin.site.register(ProfRating)
admin.site.register(Complaints)
admin.site.register(Employee)
admin.site.register(Liker)
