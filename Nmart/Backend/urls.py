from django.urls import path
from Backend import views
urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('savedata/',views.savedata,name="savedata"),
    path('categorydisplaypage/',views.categorydisplaypage,name="categorydisplaypage"),
    path('editcategorypage/<int:c_id>/', views.editcategorypage, name="editcategorypage"),
    path('deletecategory/<int:c_id>/', views.deletecategory, name="deletecategory"),
    path('update_category/<int:c_id>/', views.update_category, name="update_category"),
    path('productpage/',views.productpage,name="productpage"),
    path('saveproductdata/',views.saveproductdata,name="saveproductdata"),
    path('productdisplaypage/',views.productdisplaypage,name="productdisplaypage"),
    path('editproductpage/<int:p_id>/',views.editproductpage,name="editproductpage"),
    path('update_product/<int:p_id>/',views.update_product,name="update_product"),
    path('deleteproduct/<int:p_id>/',views.deleteproduct,name="deleteproduct"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('contactdisplaypage/',views.contactdisplaypage,name="contactdisplaypage"),
    path('deletecontact/<int:p_id>/',views.deletecontact,name="deletecontact"),


]
