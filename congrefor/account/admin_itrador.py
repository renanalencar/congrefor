from django.contrib import admin

from account.models import Account, SignupCode, AccountDeletion

from congrefor.account.models import Account

class AccountAdmin(admin.ModelAdmin):
    
    list_display = ["username", "payment", "created"]
    search_fields = ["username", "email"]
    list_filter = ["created"]

class SignupCodeAdmin(admin.ModelAdmin):
    
    list_display = ["code", "max_uses", "use_count", "expiry", "created"]
    search_fields = ["code", "email"]
    list_filter = ["created"]


admin.site.register(Account)
admin.site.register(SignupCode, SignupCodeAdmin)
admin.site.register(AccountDeletion, list_display=["email", "date_requested", "date_expunged"])
