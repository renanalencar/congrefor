from django.contrib import admin

from .models import Payment
        
from django.contrib.auth.models import User

class PaymentAdmin(admin.ModelAdmin):
    
    fields = ('date', 'time', 'note', 'confirmation', 'email')
    list_display = ('email', 'nome', 'sobrenome', 'date', 'time', 'confirmation')
    search_fields = ("email__email", "email__user__username", "email__user__first_name")
    list_filter = ["date", "confirmation"]
    
    #def queryset(self, request):
    #    qs = super(PaymentAdmin, self).queryset(request)
    #    return qs.filter(user=request.user)
    
    #def save_model(self, request, obj, form, change):
    #    obj.user = request.user
    #    obj.save()
    
    def nome(self, email):
        try:
            return User.objects.get(pk=email.email_id).first_name
        except User.DoesNotExist:
            return None
        
    def sobrenome(self, email):
        try:
            return User.objects.get(pk=email.email_id).last_name
        except User.DoesNotExist:
            return None

admin.site.register(Payment, PaymentAdmin)