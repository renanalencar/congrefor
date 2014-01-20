from django.contrib import admin

from .models import Payment
        
#admin.site.register(Payment)

class PaymentAdmin(admin.ModelAdmin):
    
    fields = ('date', 'time', 'note', 'confirmation', 'email')
    list_display = ('email', 'date', 'time', 'confirmation')
    #search_fields = ('email',)
    list_filter = ["date", "confirmation"]
    
    #def queryset(self, request):
    #    qs = super(PaymentAdmin, self).queryset(request)
    #    return qs.filter(user=request.user)
    
    #def save_model(self, request, obj, form, change):
    #    obj.user = request.user
    #    obj.save()

admin.site.register(Payment, PaymentAdmin)