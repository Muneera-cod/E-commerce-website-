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
    fs.save(r"C:\Users\LENOVO\OneDrive\Desktop\project\untitled\media\photo\\"+dt+'.jpg',dressphoto)
    path = '/media/photo/'+dt+'.jpg'
    dressprice=request.POST['textfield2']
    details=request.POST['textarea']
    count=request.POST['textfield4']
    obj=dress()
    obj.DRESS_CATEGORY_id=category
    obj.dressname=dressname
    obj.dressphoto=path
    obj.dressprice=dressprice
    obj.details=details
    obj.count=count
    obj.save()
    return HttpResponse("<script>alert('Added dress successfully');window.location='/viewdress#abc'</script>")

def viewdress(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/viewdress'</script>")
    data=dress.objects.all()
    return render(request,'admin/ViewDress.html',{"data":data})




def editdress(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/viewdress'</script>")
    data=dress.objects.get(id=id)
    datas = dress_category.objects.all()

    return render(request,'admin/EditDress.html',{"data":data,"id":id,"datas":datas})

def editdress_post(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/viewdress'</script>")
    category = request.POST['select']
    dressname = request.POST['textfield']
    dressprice = request.POST['textfield2']
    details = request.POST['textarea']
    count = request.POST['textfield4']
    if 'fileField' in request.FILES:
        dressphoto = request.FILES['fileField']  # filefield
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\LENOVO\OneDrive\Desktop\project\untitled\media\photo\\" + dt + '.jpg', dressphoto)
        path = '/media/photo/' + dt + '.jpg'
        dress.objects.filter(id=id).update(dressphoto=path)
        return HttpResponse("<script>alert('Updated dress successfully');window.location='/viewdress#abc'</script>")
    else:
        dress.objects.filter(id=id).update(DRESS_CATEGORY=category,dressname=dressname,dressprice=dressprice,details=details,count=count)
        return HttpResponse("<script>alert('Updated dress successfully');window.location='/viewdress#abc'</script>")





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

def view_ratings(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=rating.objects.all()
    ar_rt = []
    for im in data:
        a = float(im.ratings)
        fs = "/media/star/full.jpg"
        hs = "/media/star/half.jpg"
        es = "/media/star/empty.jpg"
        ar = []

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]


        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]


        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]


        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]


        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]


        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]


        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]


        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]


        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]


        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]


        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]

        ar_rt.append({
            'rating': ar,
            'DRESS':im.DRESS,
            'USER':im.USER,
            'date':im.date
        })

    return render(request, 'admin/view_Rating.html',{"data":ar_rt})
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
    data = login.objects.filter(username =email)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');window.location='/'</script>")
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
        return HttpResponse("<script>alert('Registered Successfully');window.location='/'</script>")

def user_home(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return render(request,'user/userindex.html')
def viewdressuser(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=dress.objects.all()
    d= dress_category.objects.all()
    return render(request,'user/ViewDressUser.html',{"data":data,"d":d})

def viewdressusersearch(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    data=dress.objects.filter(DRESS_CATEGORY=request.POST['select'])
    d = dress_category.objects.all()
    return render(request, 'user/ViewDressUser.html', {"data": data, "d": d})

def addtocart(request,id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    return render(request,'user/QuatityCart.html',{"id":id})
def addtocart_post(request,i):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    # print(request.session['lid'])
    count=request.POST['textfield']
    d = dress.objects.get(id = i)
    if int(d.count) >= int(count):
        qry=cart.objects.filter(DRESS=i,USER = user.objects.get(LOGIN=request.session['lid']))
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
            q=dress.objects.filter(id=i.DRESS.id)
            qty = int(q[0].count) - int(i.count)
            q.update(count=qty)
        cart.objects.filter(USER=user.objects.get(LOGIN=request.session['lid'])).delete()

        return redirect('/online/' + am + '/' + str(orderid) + '#abc')

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
        for i in qry1:
            obj1=order_sub()
            obj1.count=i.count
            obj1.DRESS_id=i.DRESS_id
            obj1.ORDER_id=obj.id
            obj1.save()
            q = dress.objects.filter(id=i.DRESS.id)
            qty = int(q[0].count) - int(i.count)
            q.update(count=qty)
        cart.objects.filter(USER=user.objects.get(LOGIN=request.session['lid'])).delete()
        return redirect('/online/'+am+'/'+str(ooid)+'#abc')

def online(request,am,ooid):
    return render(request, 'user/payorder.html', {"amount": am, "orderid": ooid})


def orderchoose_post(request,am,oid):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired please login again');window.location='/'</script>")
    payment_mode=request.POST['RadioGroup1']
    if payment_mode =="Offline":
        order.objects.filter(id=oid).update(paymentstatus="Offline",paymentdate=datetime.datetime.now().strftime("%Y-%m-%d"))
        return HttpResponse("<script>alert('Payment Successfull');window.location='/user_home'</script>")
    else:
        return redirect('/pay/'+am+'/'+str(oid)+'#abc')
def pay(request,am,oid):
    return render(request, 'user/orderbank.html', {"am": am, "oid": oid})

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
            return HttpResponse("<script>alert('Insufficient balance');window.location='/pay/"+request.session['am']+"/"+request.session['oid']+"#abc'</script>")
    else:
        return HttpResponse("<script>alert('Wrong bank details');window.location='/pay/" + request.session['am'] + "/" +request.session['oid'] + "#abc'</script>")


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
    data=order_sub.objects.filter(ORDER=id)
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



#
def view_rating(request,id):
    data=rating.objects.filter(DRESS=id)
    # qry="select rating.*,customer.* from rating,customer where customer.lid=rating.user_id"
    ar_rt = []
    for im in data:
        a = float(im.ratings)
        fs = "/media/star/full.jpg"
        hs = "/media/star/half.jpg"
        es = "/media/star/empty.jpg"
        ar = []

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]


        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]


        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]


        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]


        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]


        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]


        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]


        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]


        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]


        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]


        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]

        ar_rt.append({
            'rating': ar,
            'DRESS':im.DRESS,
            'USER':im.USER,
            'date':im.date
        })
    return render(request,"admin/vew app raiting.html",{"data":ar_rt})


def bankacc(request):
    data = bank.objects.filter(LOGIN=request.session['lid'])
    return render(request, "user/bank.html",{"data":data})


def bankaccpost(request):
    bankname = request.POST['textfield']
    accountnumber = request.POST['textfield2']
    ifsc_code = request.POST['textfield3']
    qry = bank.objects.filter(bank_name=bankname, account_no=accountnumber, ifsc_code=ifsc_code,
                              LOGIN=request.session['lid'])
    if qry.exists():
        return HttpResponse("<script>alert('Account already exists');window.location='/bankacc#abc'</script>")
    b = bank()
    b.bankbalance = '1000000'
    b.bank_name = bankname
    b.ifsc_code = ifsc_code
    b.account_no =accountnumber
    b.LOGIN_id = request.session['lid']
    b.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/bankacc#abc'</script>")


def delba(request,id):
    bank.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Removed successfully');window.location='/bankacc#abc'</script>")