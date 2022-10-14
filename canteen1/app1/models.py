from django.db import models

# Create your models here.
uid=0

class users_reg(models.Model):
    uid=models.CharField(max_length=8,primary_key=True,)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    depart=models.CharField(max_length=30)

    def __str__(self):
     return (self.uid+' '+self.f_name + ' ' + self.l_name).upper()





class users_login(models.Model):
    uid2= models.CharField(primary_key=True,max_length=8)
    email = models.CharField(max_length=30, unique=True, )
    password = models.CharField(max_length=15)
    type = models.CharField(max_length=10)



class department(models.Model):
   depart=models.CharField(max_length=30,unique=True)

   def __str__(self):
       return (self.depart)




class  staff_reg(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    email = models.CharField(max_length=30, unique=True, )
    password = models.CharField(max_length=15)





class type(models.Model):
    T_id = models.AutoField(primary_key=True)
    type=models.CharField(max_length=15,unique=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return (self.type)


class items(models.Model):
    I_id= models.AutoField(primary_key=True)
    person = models.ForeignKey("staff_reg", on_delete=models.CASCADE)
    Type = models.ForeignKey("type", on_delete=models.CASCADE)
    item = models.CharField(max_length=15,unique=True)
    price = models.IntegerField()
    stock=models.IntegerField()
    image = models.ImageField(upload_to='images',null=True)

    def __str__(self):
     return ( self.item)

class s_items(models.Model):
    s_id= models.AutoField(primary_key=True)
    person = models.ForeignKey("staff_reg", on_delete=models.CASCADE)
    item = models.CharField(max_length=15,unique=True)
    price = models.IntegerField()
    stock=models.IntegerField()
    image = models.ImageField(upload_to='s_items/%m',null=True)

    def __str__(self):
     return ( self.item)







