import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

#
def log(request):
    return render(request,'index.html')

def log_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']

    data = login.objects.filter(username = username,password= password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lin'] = '1'
        if data.usertype == 'admin':
            return redirect('/admin_home')
        else:
            return redirect('/user_home')

    else:
        return HttpResponse("<script>alert('Invalid User');window.location='/log'</script>")



def admin_home(request):

    if  request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return render(request,'admin/adminindex.html')



#  DRESS CATEGORY MANAGEMENT


def dress_categoryadd(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return render(request,'admin/DressCategoryAdd.html')

def dress_categoryadd_post(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    category = request.POST['textfield']

    obj = dress_category()
    obj.category = category
    obj.save()
    return HttpResponse("<script>alert('Added success');window.location='/dress_categoryadd'</script>")

def dress_categoryview(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=dress_category.objects.all()
    return render(request,'admin/DressCategoryView.html',{"data":data})


def dress_categoryedit(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data = dress_category.objects.get(id=id)
    return render(request,'admin/DressCategoryEdit.html',{"data":data,"id":id})

def dress_categoryedit_post(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    category=request.POST['textfield']
    dress_category.objects.filter(id=id).update(category=category)
    return HttpResponse("<script>alert('Updated Successfully');window.location='/dress_categoryview'</script>")

def dress_category_delete(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    dress_category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted sucessfully');window.location='/dress_categoryview'</script>")

 #DRESS MANAGEMENT
def add_dress(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data = dress_category.objects.all()
    return render(request,'admin/AddDress.html',{"data":data})

def add_dress_post(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    category=request.POST['select']
    dressname=request.POST['textfield']
    dressphoto=request.FILES['fileField']   # filefield
    fs=FileSystemStorage()
    dt=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\LENOVO\Desktop\project\untitled\media\photo\\"+dt+'.jpg',dressphoto)
    path = '/media/photo/'+dt+'.jpg'
    dressprice=request.POST['textfield2']
    details=request.POST['textfield3']
    count=request.POST['textfield4']
    obj=dress()
    obj.DRESS_CATEGORY_id=category
    obj.dressname=dressname
    obj.dressphoto=path
    obj.dressprice=dressprice
    obj.details=details
    obj.count=count
    obj.save()
    return HttpResponse("<script>alert('Added dress successfully');window.location='/add_dress'</script>")

def viewdress(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=dress.objects.all()
    return render(request,'admin/ViewDress.html',{"data":data})




def editdress(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=dress.objects.get(id=id)
    datas = dress_category.objects.all()

    return render(request,'admin/EditDress.html',{"data":data,"id":id,"datas":datas})

def editdress_post(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    category = request.POST['select']
    dressname = request.POST['textfield']


    dressprice = request.POST['textfield2']

    details = request.POST['textfield3']

    count = request.POST['textfield4']
    if 'fileField' in request.FILES:
        dressphoto = request.FILES['fileField']  # filefield
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\LENOVO\Desktop\project\untitled\media\photo\\" + dt + '.jpg', dressphoto)
        path = '/media/photo/' + dt + '.jpg'
        dress.objects.filter(id=id).update(dressphoto=path)
        return HttpResponse("<script>alert('Updated dress successfully');window.location='/viewdress'</script>")
    else:
        dress.objects.filter(id=id).update(DRESS_CATEGORY=category,dressname=dressname,dressprice=dressprice,details=details,count=count)
        return HttpResponse("<script>alert('Updated dress successfully');window.location='/viewdress'</script>")





def dress_delete(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    dress.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted dress Successfully').window.location='/viewdress'</script>")


def view_order(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=order.objects.all()
    return render(request,'admin/view_order.html',{"data":data})
def orderd_item(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=order_sub.objects.filter(ORDER_id=id)
    print(data)
    return render(request,'admin/OrderedItem.html',{"data":data})

def view_rating(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=rating.objects.all()

    return render(request, 'admin/view_Rating.html',{"data":data})
def change_password(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return  render(request,'admin/Change_password.html')

def change_password_post(request):
   if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
   current_password=request.POST['textfield']
   new_password=request.POST['textfield2']
   reenter_password=request.POST['textfield3']
   data=login.objects.filter(password=current_password)
   if data.exists():
       if new_password==reenter_password:
           login.objects.filter(usertype='admin').update(password=new_password)
           return HttpResponse("<script>alert('Password Changed sucessfully');window.location='/admin_home'</script>")
       else:
           return HttpResponse("<script>alert('new pasword and re-entered password not equal');window.location='/admin_home'</script>")


   else:
       return HttpResponse("<script>alert('Password is incorrect');window.location='/change_password'</script>")


def previoushistory(request):
   if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
   data=order.objects.filter(Q(paymentstatus='Offline')|Q(paymentstatus='Online')|Q(date__lt= datetime.datetime.now().strftime("%Y-%m-%d")))
   return render(request,'admin/previoushistory.html',{"data":data})




# USER MODULE
#
def registeration(request):
    return render(request,'user/Registeration.html')
def registration_post(request):
    username=request.POST['textfield']
    phonenumber=request.POST['textfield5']
    email=request.POST['textfield4']
    password=request.POST['textfield2']
    # reenter=request.POST['textfield3']
    data = login.objects.filter(username = username,password=password)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');windows.location='/log'</script>")
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.usertype = 'user'
        log_obj.save()
        obj=user()
        obj.username=username
        obj.phonenumber=phonenumber
        obj.email=email
        obj.LOGIN = log_obj
        obj.save()
        return HttpResponse("<script>alert('Registered Successfully');windows.location='/log'</script>")

def user_home(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return render(request,'user/userindex.html')
def viewdressuser(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=dress.objects.all()
    return render(request,'user/ViewDressUser.html',{"data":data})
def addtocart(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return render(request,'user/QuatityCart.html',{"id":id})
def addtocart_post(request,i):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    count=request.POST['textfield']
    d = dress.objects.get(id = i)
    if int(d.count) >= int(count):
        qry=cart.objects.filter(DRESS=i)
        if qry.exists():
            q=int(qry[0].count)+int(count)
            qry.update(count = q)
        else:

            obj=cart()
            obj.count=count
            obj.DRESS_id = i
            obj.USER = user.objects.get(LOGIN=request.session['lid'])
            obj.save()
        return HttpResponse("<script>alert('Added to cart Succesfully');window.location='/viewdressuser'</script>")
    else:
        return HttpResponse("<script>alert('Not available');window.location='/viewdressuser'</script>")
def viewcart(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=cart.objects.filter(USER__LOGIN=request.session['lid'])
    s = 0
    for i in data:
        s = int(i.count)*int(i.DRESS.dressprice)+s
    return render(request,'user/ViewCart.html',{"data":data,"s":s})


def delete_cartitem(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    cart.objects.get(id=id).delete()
    return HttpResponse("<script>alert('cart Item deleted succesfully');window.location='/viewcart'</script>")

def orderbyuseraddress(request,am):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return render(request,'user/OrDer.html',{"am":am})
def orderbyuseraddress_post(request,am):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    housename=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']

    qry=order.objects.filter(USER__LOGIN=request.session['lid'],paymentstatus="pending")
    if qry.exists():
        orderid=qry[0].id
        qry1 = cart.objects.filter(USER__LOGIN=request.session['lid'])
        for i in qry1:
            obj1 = order_sub()
            obj1.count = i.count
            obj1.DRESS_id = i.DRESS_id
            obj1.ORDER_id = orderid
            obj1.save()
        cart.objects.filter(USER=user.objects.get(LOGIN=request.session['lid'])).delete()

        return render(request, 'user/payorder.html',{"amount":am,"orderid":orderid})

    else:
        obj=order()
        obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
        obj.housename=housename
        obj.place=place
        obj.post=post
        obj.pincode=pin
        obj.paymentstatus="pending"
        obj.paymentdate="pending"
        obj.amount=am
        obj.USER=user.objects.get(LOGIN=request.session['lid'])
        obj.save()
        qry1=cart.objects.filter(USER__LOGIN=request.session['lid'])
        ooid=obj.id
        print(ooid)
        for i in qry1:
            obj1=order_sub()
            obj1.count=i.count
            obj1.DRESS_id=i.DRESS_id
            obj1.ORDER_id=obj
            obj1.save()
        cart.objects.filter(USER=user.objects.get(LOGIN=request.session['lid'])).delete()
        return render(request, 'user/payorder.html',{"amount":am,"orderid":ooid})


def orderchoose_post(request,am,oid):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    payment_mode=request.POST['RadioGroup1']
    if payment_mode =="Offline":
        order.objects.filter(id=oid).update(paymentstatus="Offline",paymentdate=datetime.datetime.now().strftime("%Y-%m-%d"))
        return HttpResponse("<script>alert('Payment Successfull');window.location='/user_home'</script>")
    else:
        return render(request,'user/orderbank.html',{"am":am,"oid":oid})
def orderbank(request,am,oid):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    request.session['am']=am
    request.session['oid']=oid
    bankname=request.POST['textfield']
    accountnumber=request.POST['textfield2']
    ifsc_code=request.POST['textfield3']
    qry=bank.objects.filter(bank_name=bankname,account_no=accountnumber,ifsc_code=ifsc_code,LOGIN=request.session['lid'])
    if qry.exists():
        total_bank_balance=qry[0].bankbalance
        if int(total_bank_balance) >= int(am):
            minus_amount=int(total_bank_balance)-int(am)
            bank.objects.filter(LOGIN=request.session['lid']).update(bankbalance=minus_amount)
            qry1=bank.objects.get(LOGIN=1)
            admin_total_balance=qry1.bankbalance
            plus_amount=int(admin_total_balance)+int(am)
            bank.objects.filter(LOGIN=1).update(bankbalance=plus_amount)
            order.objects.filter(id=oid).update(paymentstatus="Online",paymentdate=datetime.datetime.now().strftime("%Y-%m-%d"))
            return HttpResponse("<script>alert('Payment Successfull');window.location='/user_home'</script>")
        else:
            return HttpResponse("<script>alert('Insufficient balance');window.location='/orderbank/"+request.session['am']+"/"+request.session['oid']+"'</script>")
    else:
        return HttpResponse("<script>alert('Wrong bank details');window.location='/orderbank/" + request.session['am'] + "/" +request.session['oid'] + "'</script>")


def changepassword(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return  render(request,'user/Change_password.html')

def changepassword_post(request):
   if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
   current_password=request.POST['textfield']
   new_password=request.POST['textfield2']
   reenter_password=request.POST['textfield3']
   data=login.objects.filter(password=current_password)
   if data.exists():
       if new_password==reenter_password:
           login.objects.filter(usertype='user',id = request.session['lid']).update(password=new_password)
           return HttpResponse("<script>alert('Password Changed sucessfully');window.location='/user_home'</script>")
       else:
           return HttpResponse("<script>alert('new pasword and re-entered password not equal');window.location='/user_home'</script>")


   else:
       return HttpResponse("<script>alert('Password is incorrect');window.location='/changepassword'</script>")


def viewprofile(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=user.objects.get(LOGIN=request.session['lid'])
    return render(request,'user/Viewprofile.html',{"data":data})

def vieworder(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=order.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/Orderpay.html',{"data":data})
def orderitems(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=order_sub.objects.filter(id=id)
    d = []
    for i in data:
        d.append(
            {
                'ORDER':i.ORDER,
                'DRESS':i.DRESS,
                'count':i.count,
                't':int(i.count)*int(i.DRESS.dressprice)
            }
        )
    return render(request,'user/OrderView.html',{"data":d})



def logout(request):
    request.session['lin'] = '0'
    return HttpResponse("<script>alert('Logout successfulyy');window.location='/'</script>")

def rate(request,id):
    return render(request,'user/rate.html',{"id":id})
def rate_post(request,id):
    star=request.POST['star']
    date=datetime.datetime.now().strftime("%Y-%m-%d")
    obj=rating()
    obj.ratings=star
    obj.date=date
    obj.USER=user.objects.get(LOGIN=request.session['lid'])
    obj.DRESS=dress.objects.get(id=id)
    obj.save()
    return HttpResponse("<script>alert('Rating Submitted');window.location='/user_home'</script>")
