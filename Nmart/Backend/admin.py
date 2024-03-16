from django.contrib import admin

# Register your models here.
from Backend.models import categorydb,productdb
admin.site.register(categorydb)
admin.site.register(productdb)
