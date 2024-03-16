from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from Backend.models import categorydb, productdb
from Frontend.models import contactdb


# Create your views here.
def indexpage(request):
    messages.success(request, "Login successfully")
    return render(request,"index.html")
def categorypage(request):

    return render(request,"Add category.html")
def savedata(request):
    if request.method=="POST":
        a=request.POST.get('name')
        img=request.FILES['image']

        c=request.POST.get('description')
        obj=categorydb(CategoryName =a,CategoryImage =img,Description=c)
        obj.save()
        messages.success(request, "Category Added successfully")
        return redirect(categorypage)

def categorydisplaypage(request):
    cat=categorydb.objects.all()

    return render(request,"Category display.html",{'cat':cat})

def editcategorypage(request, c_id):
    data=categorydb.objects.get(id=c_id)

    return render(request,"Edit category .html",{'data':data})


def deletecategory(request,c_id):
    data=categorydb.objects.filter(id=c_id)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(categorydisplaypage)



def update_category(request,c_id):
    if request.method=="POST":
        x=request.POST.get('name')
        y = request.POST.get('description')
        try:
            img1 = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=c_id).CategoryImage

    categorydb.objects.filter(id=c_id).update(CategoryName=x, CategoryImage=file, Description=y)
    return redirect(categorydisplaypage)
def productpage(request):
    return render(request,"Addproducts.html")
def saveproductdata(request):
    if request.method == "POST":
        h=request.POST.get('category')
        i=request.POST.get('productname')
        j=request.POST.get('price')
        k = request.POST.get('description')
        img2=request.FILES['image']

        obj=productdb(CategoryName =h, ProductName=i,Price=j,Description=k,ProductImage =img2)
        obj.save()
        messages.success(request, "Product saved successfully")
        return redirect(productpage)
def productdisplaypage(request):

    pro=productdb.objects.all()
    return render(request, "Display products.html",{'pro':pro})

def editproductpage(request,p_id):
    pro=productdb.objects.get(id=p_id)
    return render(request,"Edit products.html",{'pro': pro})

def update_product(request, p_id):
    if request.method=="POST":
        q = request.POST.get('category')
        r = request.POST.get('productname')
        s = request.POST.get('price')
        t = request.POST.get('description')

        try:
            img3 = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=p_id).ProductImage

    productdb.objects.filter(id=p_id).update(CategoryName =q, ProductName=r,Price=s,Description=t,ProductImage =file)
    messages.success(request, "Updated...")
    return redirect(productdisplaypage)
def deleteproduct(request,p_id):
    data=productdb.objects.filter(id=p_id)
    data.delete()
    messages.success(request, "Deleted")
    return redirect(productdisplaypage)
def adminpage(request):
    return render(request,"Admin_login.html")
def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        up = request.POST.get('password')


        if User.objects.filter(username=un).exists():
            x = authenticate(username=un, password=up)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=up

                return redirect(indexpage)
            else:
                return redirect(adminpage)
        else:
            return redirect(adminpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminpage)

def contactdisplaypage(request):

    data=contactdb.objects.all()
    return render(request, "Display contact.html",{'data': data})
def deletecontact(request,p_id):
    data = contactdb.objects.filter(id=p_id)
    data.delete()
    return redirect(contactdisplaypage)

