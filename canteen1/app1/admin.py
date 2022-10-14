from django.contrib import admin
from .models import users_reg,users_login,type,items,department,s_items,staff_reg
from django.contrib.auth.models import Group,User

# Register your models here.


admin.site.site_header  =  "Canteen admin"
admin.site.site_title  =  "AJCE canteen admin site"
admin.site.index_title  =  "Canteen Management Admin"

class Adminuserreg(admin.ModelAdmin):
    list_display=['uid','f_name','l_name','mobile','depart']
    list_per_page = 5
    search_fields = ('f_name',)

class AdminDepartrment(admin.ModelAdmin):
    list_display=['depart']
    list_per_page = 5
    search_fields = ('depart',)

class Adminstaff_reg(admin.ModelAdmin):
    list_display=['f_name','l_name','mobile','email']
    list_per_page = 5
    search_fields = ('f_name',)



admin.site.register(users_reg, Adminuserreg )
admin.site.register(type,)
admin.site.register(items,)
admin.site.register(s_items,)
admin.site.register(staff_reg,Adminstaff_reg)

admin.site.register(department,AdminDepartrment)


admin.site.unregister(Group)
admin.site.unregister(User)
