from django.db import models # database thaka model k import kora hoyasa..
from django.contrib.auth.models import User # django thaka built-in user k import kora hoyasa.
# Create your models here.

# ACCOUNT_TYPE=(
#     ('Savings','Savings'),
#     ('Current','Current'),
    
# )
# GENDER_TYPE=(
#     ('Male','Male'),
#     ('Female','Female'),
# )


from . constants import ACCOUNT_TYPE,GENDER_TYPE # this is for best practice.
class UserBankAccount(models.Model):
    user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE) # inside of User, User holds-> username, pas,email.etc in builtin. || OneToOneField = username,pass, etc is unique. 
    account_type=models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no=models.IntegerField(unique=True) # unique=True, account number is must unique for every person
    birth_date=models.DateField(null=True,blank=True) # null=True and blank=True = kaw na detachila faka rakbe.
    gender=models.CharField(max_length=10,choices=GENDER_TYPE)
    initial_deposit_date=models.DateField(auto_now_add=True) # auto_now_add = initial date ta save rakbe.
    balance=models.DecimalField(default=0,max_digits=12,decimal_places=2) # decimal_places = after point it's kept two digit.
    def __str__(self):
        return str(self.account_no)  # this function is used for showing UserBankAccount clearly such as like account_no in database.

class UserAddress(models.Model):
    user=models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100,null=True)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100,default='rajshahi')
    def __str__(self):
        return(self.user.email)
    
