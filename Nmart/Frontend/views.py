from django.contrib import messages
from django.shortcuts import render, redirect
from Backend.models import productdb,categorydb
from Frontend.models import contactdb, logindb, cartdb, checkoutdb


# Create your views here.
def homepage(request):
    pro=productdb.objects.all()
    cat=categorydb.objects.all()
    data = cartdb.objects.filter(Username=request.session['Name'])

    return render(request,"Homepage.html",{'pro':pro, 'cat':cat,'data':data})
def shopproductpage(request):
    pro = productdb.objects.all()
    cat = categorydb.objects.all()
    data = cartdb.objects.filter(Username=request.session['Name'])
    return render(request,"Shop products.html",{'pro':pro,'cat':cat,'data':data})
def categoriespage(request, catname):
    pro=productdb.objects.filter(CategoryName=catname)
    cat=categorydb.objects.all()
    data = cartdb.objects.filter(Username=request.session['Name'])
    return render(request,"Categories.html",{'pro':pro,'cat':cat,'data':data})
def singleproductpage(request, proid):
    data = cartdb.objects.filter(Username=request.session['Name'])
    pro=productdb.objects.get(id=proid)
    cat = categorydb.objects.all()
    return render(request,"Singleproduct.html",{'pro':pro,'cat':cat,'data':data})
def blogpage(request):
    data = cartdb.objects.filter(Username=request.session['Name'])
    return render(request,"Blog.html",{'data':data})
def contactpage(request):
    cat = categorydb.objects.all()
    data = cartdb.objects.filter(Username=request.session['Name'])
    return render(request,"contact.html",{'cat':cat,'data':data})
def savecontactdata(request):
    if request.method=="POST":
        m =request.POST.get('name')

        n =request.POST.get('email')
        o =request.POST.get('message')
        obj =contactdb(Name=m,Email=n,Message=o)
        obj.save()
        return redirect(contactpage)
def loginpage(request):

    return render(request,"Loginpage.html")
def registerpage(request):
    return render(request,"Register.html")

def savelogindata(request):
    if request.method=="POST":
       v= request.POST.get('username')
       w= request.POST.get('password')
       x=request.POST.get('email')
       obj=logindb(Name=v,Password=w,Email=x)
       obj.save()

       return redirect(loginpage)
def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd= request.POST.get('password')
        em= request.POST.get('email')

        if logindb.objects.filter(Name=un,Password=pwd,Email=em).exists():

            request.session['Name']=un
            request.session['Password']=pwd
            request.session['Email']=em

            messages.success(request, "Login succesfully")
            return redirect(homepage)
        else:

            return redirect(loginpage)
    else:

        return redirect(loginpage)

def userlogout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(loginpage)
def cartpage(request):


     data = cartdb.objects.filter(Username=request.session['Name'])
     total_price = 0
     for i in data:
        total_price = total_price + i.TotalPrice
     return render(request, "cart.html", {'data': data,'total_price': total_price})

def savecartdata(request):

    if request.method == "POST":
         l= request.POST.get('name')

         m= request.POST.get('productname')
         n= request.POST.get('quantity')
         o=request.POST.get('price')
         p=request.POST.get('totalprice')


         obj = cartdb(Username=l,Productname=m,Quantity=n,Price=o,TotalPrice=p)
         obj.save()
         messages.success(request, "Add to cart succesfully")
         return redirect(homepage)
def checkoutpage(request):
    cart = cartdb.objects.filter(Username=request.session['Name'])
    total_price = 0
    for i in cart:
        total_price = total_price + i.TotalPrice
    return render(request, "checkout.html", {'cart': cart, 'total_price': total_price})



def cart_delete(request,p_id):
    x=cartdb.objects.filter(id=p_id)
    x.delete()
    return redirect(cartpage)
def savecheckoutdata(request):

    if request.method == "POST":
         fn= request.POST.get('firstname')
         ln= request.POST.get('lastname')
         cn= request.POST.get('state')
         sr=request.POST.get('street')
         cy=request.POST.get('city')
         po=request.POST.get('post')
         ph=request.POST.get('phone')
         em=request.POST.get('email')






         obj = checkoutdb( FirstName=fn,LastName=ln,Country=cn,Street=sr,Town=cy,Postcode=po, Phone=ph, Email=em,)
         obj.save()
         messages.success(request, "Order Placed")
         return redirect(checkoutpage)
