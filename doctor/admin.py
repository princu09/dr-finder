# Custom User Create
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Import Models
from .models import CustomUser , HealthCard , BookAppoinment , Prescriptions , MedicalReports , Bill

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username', 'first_name', 'last_name']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'fieldName', 'gender',
                           'mobile', 'dob' , 'bloodGroup', 'address', 'city', 'state', 'status' ,'healthCard', 'healthCardAcceptByAdmin', 'userImg', 'token' ,)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fieldName', 'gender', 'mobile',
                           'dob', 'bloodGroup', 'address', 'city', 'state', 'status' ,'healthCard','healthCardAcceptByAdmin', 'userImg', 'token')}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(HealthCard)
admin.site.register(BookAppoinment)
admin.site.register(Prescriptions)
admin.site.register(MedicalReports)
admin.site.register(Bill)