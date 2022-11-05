from django.shortcuts import render,redirect
from .models import users_reg,users_login,type,items,department,staff_reg,teachers,cart1
from django.contrib import messages
from django.contrib.auth import login,logout

#  Create your views here.




def index(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")

        if users_login.objects.filter(email=email, password=password).exists():
            a = users_login.objects.get(email=email)
            uid = a.uid2
            if users_reg.objects.filter(uid=uid).exists():
                request.session['email'] = email
                request.session['password'] = password
                return redirect('user1/')
            else:
                messages.error(request, '----invalid credentials----')
                return redirect('/home/')

        elif teachers.objects.filter(email=email, password=password).exists():
            request.session['email'] = email
            request.session['password'] = password
            return redirect('user1/')
        elif staff_reg.objects.filter(email=email, password=password).exists():
            request.session['email'] = email
            request.session['password'] = password
            return redirect('staff_item_add/')
        else:
            messages.error(request, '----invalid credentials----')
            return redirect('/home/')
    return render (request,"logpage.html")


# def home(request):
#     request.session['email'] = 'null'
#     request.session['password'] = 'null'
#     return render(request, "logpage.html")




def login1(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'

    # if request.method == "POST":
    #     email=request.POST.get("email")
    #     password =request.POST.get("pass")
    #
    #
    #     if users_login.objects.filter(email=email,password=password).exists():
    #          a=users_login.objects.get(email=email)
    #          uid=a.uid2
    #          if users_reg.objects.filter(uid=uid).exists():
    #             request.session['email']=email
    #             request.session['password']=password
    #             return redirect ('user1/')
    #          else:
    #              messages.error(request, '----invalid credentials----')
    #              return redirect('/login/')
    #
    #     elif teachers.objects.filter(email=email, password=password).exists():
    #         request.session['email'] = email
    #         request.session['password'] = password
    #         return redirect('user1/')
    #     elif staff_reg.objects.filter(email=email, password=password).exists():
    #         request.session['email'] = email
    #         request.session['password'] = password
    #         return redirect('staff/')
    #     else:
    #          messages.error(request,'----invalid credentials----')
    #          return redirect('/login/')
    # return render(request,'login.html')




def user1(request):

   if request.session['email'] == 'null':
       return redirect('/home/')
   # id=request.session['uid']
   elif 'email' in request.session:
     email=request.session['email']
     f_item=""
     list_items = items.objects.all()
     if request.method == "POST":
             fil_item=request.POST.get("fil_item")
             fil_type=request.POST.get("fil_type")
             if fil_type=='null' and fil_item=='':
                 list_items = items.objects.all()
             elif fil_type=='null' and fil_item!='' :
                 list_items = items.objects.filter(item__icontains=fil_item)
             elif fil_item=='' and fil_type!='null':
                 list_items = items.objects.filter(Type_id=fil_type)
             else:
                list_items=items.objects.filter(item=fil_item , Type_id=fil_type)

         #    list_items = items.objects.filter(Type_id=fi_item)

     content1= {
         'l_det': users_login.objects.filter(email=email),
         'r_det': users_reg.objects.all(),
         # 's_det':s_items.objects.all(),
         'staff':staff_reg.objects.filter(email=email),
         'teacher': teachers.objects.filter(email=email),
         't_det': type.objects.all(),
         'i_det':list_items,
         'email': email
        }
   return render(request, 'index_2.html', content1)


def shop(request):

   if request.session['email'] == 'null':
       return redirect('/home/')
   # id=request.session['uid']
   elif 'email' in request.session:
     email=request.session['email']
     f_item=""
     list_items = items.objects.all()
     # if request.method == "POST":
     #         fil_item=request.POST.get("fil_item")
     #         fil_type=request.POST.get("fil_type")
     #         if fil_type=='null' and fil_item=='':
     #             list_items = items.objects.all();
     #         elif fil_type=='null' and fil_item!='' :
     #             list_items = items.objects.filter(item__icontains=fil_item)
     #         elif fil_item=='' and fil_type!='null':
     #             list_items = items.objects.filter(Type_id=fil_type)
     #         else:
     #            list_items=items.objects.filter(item=fil_item , Type_id=fil_type)
     #
     #        list_items = items.objects.filter(Type_id=fi_item)

     content1= {
         'l_det': users_login.objects.filter(email=email),
         'r_det': users_reg.objects.all(),
         # 's_det':s_items.objects.all(),
         'staff':staff_reg.objects.filter(email=email),
         'teacher': teachers.objects.filter(email=email),
         't_det': type.objects.all(),
         'i_det':list_items,
         'email': email
        }
   return render(request, 'shop.html', content1)


def shop1(request,id):

   if request.session['email'] == 'null':
       return redirect('/home/')
   elif 'email' in request.session:
     Types = type.objects.get(Type_id=id)
     email=request.session['email']
     f_item=""
     list_items = items.objects.filter(Type=Types)

     content1= {
         'l_det': users_login.objects.filter(email=email),
         'r_det': users_reg.objects.all(),
         # 's_det':s_items.objects.all(),
         'staff':staff_reg.objects.filter(email=email),
         'teacher': teachers.objects.filter(email=email),
         't_det': type.objects.all(),
         'i_det':list_items,
         'email': email
        }
   return render(request, 'shop.html', content1)


def search_shop(request):

   if request.session['email'] == 'null':
       return redirect('/home/')
   elif 'email' in request.session:
     Types = type.objects.get(Type_id=id)
     email=request.session['email']
     f_item=""
     list_items = items.objects.filter(Type=Types)

     content2= {
         'l_det': users_login.objects.filter(email=email),
         'r_det': users_reg.objects.all(),
         # 's_det':s_items.objects.all(),
         'staff':staff_reg.objects.filter(email=email),
         'teacher': teachers.objects.filter(email=email),
         't_det': type.objects.all(),
         'i_det':list_items,
         'email': email
        }
     return render(request, 'shop.html', content2)


def staff(request):

   if request.session['email'] == 'null':
       return redirect('/home/')
   # id=request.session['uid']
   elif 'email' in request.session:
     email=request.session['email']
     content= {

         # 's_det':s_items.objects.all(),
         'staff':staff_reg.objects.filter(email=email),
         'types': type.objects.all(),
         'items':items.objects.all(),




         'email': email
     }
     return render(request, 'staff.html', content)
   return render(request, "home.html")



def cpass(request):
   if request.session['email'] == 'null':
        return redirect('/home/')
   email = request.session['email']
   password=request.session['password']
   if request.method == "POST":
        pwd =request.POST.get("pass")
        n_pwd = request.POST.get("n_pass")
        # cn_pwd = request.POST.get("c_pwd")
        l_det= users_login.objects.get(email=email)
        password=l_det.password
        if pwd == password:
            l_det.password=n_pwd
            l_det.save()
            return redirect('/profile/')
        else:
            return redirect('/cpass/')
   l_det2= users_login.objects.get(email=email)
   uid2=l_det2.uid2
   print(uid2)
   content = {
       'l_det':l_det2,
       'r_det': users_reg.objects.get(uid=uid2),

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
        type = "Student"
        depart = request.POST.get("depart")
        email = request.POST.get("email")
        password=request.POST.get("password")
        if users_login.objects.filter(email=email).exists():
            if users_login.objects.filter(email=email).exists():
              messages.info(request,"---unsuccessfull,email or id already exists---")
              return redirect('/student/')

        else:
            new_reg=users_reg(uid=uid,first_name=f_name,last_name=l_name,mobile=mobile,depart=depart)
            new_reg.save()
            new_log = users_login(uid2=luid,type=type, email=email, password=password)
            a=new_log.save()
            return redirect('/')

   return render (request,"reg_stu.html",dep)





def profile(request):
    #reg=users_reg.objects.all()
    email=request.session['email']
    if request.session['email'] == 'null':
        return redirect('/home/')
    else :
      content={
         'l_det':users_login.objects.all(),
         'r_det':users_reg.objects.all(),
         'email':email
      }
      return render(request,"profile.html",content)



def e_profile(request):
   email = request.session['email']
   user1= users_login.objects.get(email=email)
   uid=user1.uid2
   user=users_reg.objects.get(uid=uid)

   if request.session['email'] == 'null':
        return redirect('/home/')
   else:
     content={
         'l_det':users_login.objects.all(),
         'r_det':users_reg.objects.all(),
         'd_det':department.objects.all(),
         'email':email
       }
     if request.method == "POST":
         f_name = request.POST.get("f_name")
         l_name = request.POST.get("l_name")
         mobile = request.POST.get("mobile")
         depart = request.POST.get("depart")
         user.first_name=f_name
         user.last_name = l_name
         user.mobile = mobile
         user.depart = depart
         user.save()
         return redirect('/profile/')
     return render(request,"ed_profile.html",content)


def add_cart_i(request,id):
    if request.session['email'] == 'null':
        return redirect('/home/')
    # cart_item=cart1.objects.get(Items_id=id)
    item=items.objects.get(Items_id=id)

    image=item.image.url
    person=request.session['email']
    price=item.price
    stock=item.stock
    total=price
    if stock>0:


        if cart1.objects.filter( person =person,item=item).exists():
             # item.stock -= 1
             # item.save()
             c_item1=cart1.objects.get( person =person,item=item)
             c_item1.quantity = c_item1.quantity + 1
             c_item1.total=c_item1.price * c_item1.quantity
             c_item1.save()
             return redirect('/shop/')
        else:
         # item.stock -= 1
         item.save()
         new_cart=cart1(item=item,image=image,person=person,price=price,total=total)
         new_cart.save()
         return redirect('/shop/')








def cart(request):
    if request.session['email'] == 'null':
        return redirect('/home/')
    email = request.session['email']
    cart=cart1.objects.filter(person=email)
    total=0
    for cart in cart:
        total += cart.price * cart.quantity
    content={
        'c_det' : cart1.objects.filter(person=email),
        'stotal':total
    }


    return render (request,"cart.html",content)

def u_cart(request):
    if request.session['email'] == 'null':
        return redirect('/home/')
    email=request.session['email']
    ucart=cart1.objects.filter(person=email)
    if request.method == "POST":
        for ucart in ucart:
           items=ucart.item
           item1=cart1.objects.get(person=email,item=items)
           item1.quantity = request.POST.get(item1.item.item)
           qua=item1.quantity
           print(qua)
           if qua<'0':
               item1.quantity=1
           item1.save()
           c_item1 = cart1.objects.get(person=email, item=items)
           c_item1.total = c_item1.price * c_item1.quantity
           c_item1.save()
           # stock=items.objects.get(item=item1.item)
           # stock.stock=stock.stock-c_item1.quantity
           # stock.save()


           # item.save()

    return redirect('/cart/')

def de_cart(request,id):
    if request.session['email'] == 'null':
        return redirect('/home/')
    cart1.objects.get(cart_id=id).delete()
    return redirect('/cart/')


def checkout(request):
    if request.session['email'] == 'null':
        return redirect('/home/')
    email = request.session['email']
    cart = cart1.objects.filter(person=email)
    total = 0
    for cart in cart:
        total += cart.price * cart.quantity
    content = {
        'c_det': cart1.objects.filter(person=email),
        'stotal': total
    }
    return render (request,"checkout.html",content)



def staff_item_add(request):
    if request.session['email'] == 'null':
        return redirect('/home/')
    email=request.session['email']
    types = {
        't_det':type.objects.all(),
    }
    if request.method == "POST":
        person=staff_reg.objects.get(email=email)
        ty=request.POST.get("type")
        i_type=type.objects.get(type=ty)
        item = request.POST.get("item")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        image = request.FILES.get("image")

        item.lower()
        if items.objects.filter(item=item).exists():
            messages.info(request, "---item already exists---")
            return redirect('/staff_item_add/')

        else:
            item_save=items(person=person,Type=i_type,item=item,price=price,stock=stock,image=image)
            item_save.save()
            messages.info(request, "---item added successfully---")
            return redirect('/staff_item_add/')

    return render(request, "staff_item_add.html", types)









def logout(request):
    request.session['email'] = 'null'
    request.session['password'] = 'null'
    return redirect('/home/')



