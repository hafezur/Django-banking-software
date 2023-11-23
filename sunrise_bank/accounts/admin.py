from django.contrib import admin
from . models import UserBankAccount,UserAddress # for registering UserBankAccount and UserAddress from medels.
# Register your models here.
admin.site.register(UserBankAccount) 
admin.site.register(UserAddress) 

