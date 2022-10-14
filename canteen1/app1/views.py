from django.shortcuts import render,redirect
from .models import users_reg,users_login,type,items,department,s_items
from django.contrib import messages
from django.contrib.auth import login,logout

# Create your views here.




def index(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'
    return render (request,"home.html")


def home(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'
    return render(request, "home.html")




def login1(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'

    if request.method == "POST":
        email=request.POST.get("email")
        password =request.POST.get("pass")
        user=users_login.objects.filter(email=email,password=password)
        if user:
             request.session['email']=email
             request.session['password']=password
             return redirect ('user1/')
        else:
             messages.error(request,'-- email and password was not matching... Please refresh and try again -- ')
             return redirect('/login/')
    return render(request,'login.html')




def user1(request):

   if request.session['email'] == 'null':
       return redirect('/login/')
   # id=request.session['uid']
   elif 'email' in request.session:
     email=request.session['email']
     content= {
         'l_det': users_login.objects.all(),
         'r_det': users_reg.objects.all(),
         's_det':s_items.objects.all(),


         'email': email
     }
     return render(request, 'user.html', content)
   return render(request, "home.html")





def cpass(request):

   email = request.session['email']
   password=request.session['password']
   if request.method == "POST":
        pwd =request.POST.get("pwd")
        n_pwd = request.POST.get("n_pwd")
        cn_pwd = request.POST.get("c_pwd")
        l_det= users_login.objects.all()
        for d in l_det:
         if pwd == password and n_pwd == cn_pwd:
            new_log = users_login(password=n_pwd)
            new_log.save()
            return render(request, "/profile/")
        else:
            return render(request, "/")
   if request.session['email'] == 'null':
        return redirect('/login/')
   content = {
       'l_det': users_login.objects.all(),
       'r_det': users_reg.objects.all(),

       'email': email
   }
   return render(request, "ch_pass.html",content)






def student(request):
   request.session['email'] = 'null'
   request.session['password'] = 'null'
   dep={
       'd_det': department.objects.all(),
    }
   if request.method=="POST":
        uid = request.POST.get("uid")
        luid=request.POST.get("uid")
        f_name=request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        mobile = request.POST.get("m_number")
        type = "Tea/stu"
        depart = request.POST.get("depart")
        email = request.POST.get("email")
        password=request.POST.get("password")

        new_reg=users_reg(uid=uid,f_name=f_name,l_name=l_name,mobile=mobile,depart=depart)
        new_reg.save()
        new_log = users_login(uid2=luid,type=type, email=email, password=password)
        a=new_log.save()
        if a:
            messages.error(request, '-- registration unsuccessfull  -- ')
            return redirect('/')
        else:
            messages.error(request, '-- registration unsuccessfull  -- ')
            return redirect('/student/')
   return render (request,"reg_stu.html",dep)





def profile(request):
    #reg=users_reg.objects.all()
    email=request.session['email']
    if request.session['email'] == 'null':
        return redirect('/login/')
    else :
      content={
         'l_det':users_login.objects.all(),
         'r_det':users_reg.objects.all(),
         'email':email
      }
      return render(request,"profile1.html",content)



def e_profile(request,id):
   user= users_reg.objects.get(uid=id)



   email = request.session['email']
   if request.session['email'] == 'null':
        return redirect('/login/')
   else:
     content={
         'l_det':users_login.objects.all(),
         'r_det':users_reg.objects.all(),
         'email':email
       }
     if request.method == "POST":
         f_name = request.POST.get("f_name")
         l_name = request.POST.get("l_name")
         mobile = request.POST.get("m_number")
         depart = request.POST.get("depart")



         new_reg = users_reg( uid=id,f_name=f_name, l_name=l_name, mobile=mobile, depart=depart)
         new_reg.save()

         return redirect('/profile/')
     return render(request,"ed_profile.html",content)







def logout(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'
    return redirect('/login/')



