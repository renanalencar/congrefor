from django.contrib import admin

#from account.models import Account, SignupCode, AccountDeletion
from congrefor.registration.models import Registration

class Registration(admin.ModelAdmin):
    
    list_display = ["username"]
#    search_fields = ["code", "email"]
#    list_filter = ["created"]


admin.site.register(Registration)
#admin.site.register(SignupCode, SignupCodeAdmin)
#admin.site.register(AccountDeletion, list_display=["email", "date_requested", "date_expunged"])
