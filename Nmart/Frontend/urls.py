from django.urls import path
from Frontend import views
urlpatterns=[
path('homepage/',views.homepage,name="homepage"),
path('shopproductpage/',views.shopproductpage,name="shopproductpage"),
path('categoriespage/<catname>/',views.categoriespage,name="categoriespage"),
path('singleproductpage/<int:proid>/',views.singleproductpage,name="singleproductpage"),
path('blogpage/',views.blogpage,name="blogpage"),
path('contactpage/',views.contactpage,name="contactpage"),
path('savecontactdata/',views.savecontactdata,name="savecontactdata"),
path('loginpage/',views.loginpage,name="loginpage"),
path('registerpage/',views.registerpage,name="registerpage"),
path('savelogindata/',views.savelogindata,name="savelogindata"),
path('userlogin/',views.userlogin,name="userlogin"),
path('userlogout/',views.userlogout,name="userlogout"),
path('cartpage/',views.cartpage,name="cartpage"),
path('savecartdata/',views.savecartdata,name="savecartdata"),
path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
path('savecheckoutdata/',views.savecheckoutdata,name="savecheckoutdata"),
path('cart_delete/<int:p_id>/', views.cart_delete, name="cart_delete"),

]