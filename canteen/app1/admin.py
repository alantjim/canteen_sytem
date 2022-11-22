from django.urls import path
from django.shortcuts import render
from django.contrib import admin,messages
from .models import users_reg,users_login,type,items,department,staff_reg,teachers,cart1,orders,orderplaced
from django.contrib.auth.models import Group,User
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
# Register your models here.


admin.site.site_header  =  "Canteen admin"
admin.site.site_title  =  "AJCE canteen admin site"
admin.site.index_title  =  "Canteen Management Admin"



class CsvImportForm(forms.Form):
    csv_upload=forms.FileField()


class Adminuserreg(admin.ModelAdmin):
    list_display=['uid','first_name','last_name','mobile','depart']
    list_per_page = 5
    search_fields = ('first_name',)

class AdminDepartrment(admin.ModelAdmin):
    list_display=['depart']
    list_per_page = 5
    search_fields = ('depart',)

class Adminstaff_reg(admin.ModelAdmin):
    list_display=['first_name','last_name','mobile','email','password']
    list_per_page = 5
    search_fields = ('first_name',)

    def get_urls(self):
        urls= super().get_urls()
        new_urls = [path('upload-csv/' ,self.upload_csv)]
        return new_urls + urls

    def upload_csv(self,request):
        if request.method=="POST":

            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request,'the wrong file is uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data=csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")


            for x in csv_data:
                fields = x.split(",")
                if staff_reg.objects.filter(email=fields[3]).exists():
                    messages.warning(request, "---unsuccessfull,email already exists---")
                else:
                 created = staff_reg.objects.update_or_create(

                    first_name= fields[0],
                    last_name = fields[1],
                    mobile = fields[2],
                    email = fields[3],
                    password=fields[4],
                 )




        form = CsvImportForm()
        data = {"form":form}

        return render(request,"admin/csv_upload.html",data)

class Adminteachers(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','department', 'mobile', 'email','password']
    list_per_page = 5
    search_fields = ('first_name',)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method=="POST":

            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request,'the wrong file is uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data=csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")


            for x in csv_data:
                fields = x.split(",")
                if teachers.objects.filter(email=fields[4]).exists():
                    messages.warning(request, "---unsuccessfull,email already exists---")
                else:
                    created = teachers.objects.update_or_create(

                      first_name= fields[0],
                      last_name = fields[1],
                      department=fields[2],
                      mobile = fields[3],
                      email = fields[4],
                      password=fields[5],
                    )

        form = CsvImportForm()
        data = {"form": form}

        return render(request, "admin/csv_upload.html", data)


admin.site.register(users_reg, Adminuserreg )
admin.site.register(users_login, )
admin.site.register(type,)
admin.site.register(orderplaced,)
admin.site.register(orders,)
admin.site.register(items,)
admin.site.register(cart1,)
admin.site.register(staff_reg,Adminstaff_reg)
admin.site.register(teachers,Adminteachers)
admin.site.register(department,AdminDepartrment)


admin.site.unregister(Group)
admin.site.unregister(User)