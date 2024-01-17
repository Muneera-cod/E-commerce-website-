from django.db import models

# Create your models here.class
class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class user(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.BigIntegerField()
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class dress_category(models.Model):
    category=models.CharField(max_length=200)

class dress(models.Model):
    DRESS_CATEGORY=models.ForeignKey(dress_category,default=1,on_delete=models.CASCADE)
    dressname=models.CharField(max_length=200)
    dressphoto=models.CharField(max_length=200)
    dressprice=models.CharField(max_length=200)
    details=models.CharField(max_length=200)
    count=models.CharField(max_length=200)
class cart(models.Model):
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    DRESS=models.ForeignKey(dress,default=1,on_delete=models.CASCADE)
    count=models.CharField(max_length=200)
class order(models.Model):
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    date=models.CharField(max_length=200)
    housename=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    pincode=models.CharField(max_length=200)
    paymentstatus=models.CharField(max_length=200)
    paymentdate=models.CharField(max_length=200)
    amount=models.CharField(max_length=200,default=1)
class order_sub(models.Model):
    ORDER=models.ForeignKey(order,default=1,on_delete=models.CASCADE)
    DRESS=models.ForeignKey(dress,default=1,on_delete=models.CASCADE)
    count=models.CharField(max_length=200)
class rating(models.Model):
    DRESS=models.ForeignKey(dress,default=1,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    ratings=models.CharField(max_length=200)
    date=models.CharField(max_length=200)

class bank(models.Model):
    bank_name=models.CharField(max_length=200)
    account_no=models.CharField(max_length=200)
    ifsc_code=models.CharField(max_length=200)
    bankbalance=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

