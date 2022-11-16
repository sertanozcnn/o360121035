from django.contrib import admin

# Register your models here.
from django.contrib import admin

from appSale.models import housesale,Users,Price,House_Category

admin.site.register(housesale)
admin.site.register(Users)
admin.site.register(Price)
admin.site.register(House_Category)